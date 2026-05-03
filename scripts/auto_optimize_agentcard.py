# scripts/auto_optimize_agentcard.py
from __future__ import annotations

import argparse
import copy
import json
import random
from pathlib import Path
from typing import Any, Dict, List, Tuple

from src.client.agents.http_agent_robust import HTTPAgentRobust
from scripts.card_pipeline import process_cards_for_eval
from scripts.run_all_arch import run_horizontal_with_handoff, metrics_horizontal


def load_json(p: Path) -> Any:
    return json.loads(p.read_text(encoding="utf-8"))

def write_json(p: Path, obj: Any) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


def mutate_attacker_card(cards: List[Dict[str, Any]], attacker_prefix: str, rng: random.Random) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """
    Small, controlled mutations (paper-friendly):
      - add_tag
      - replace_tag
      - append_short_phrase_to_desc
    """
    new_cards = copy.deepcopy(cards)
    idxs = [i for i, c in enumerate(new_cards) if str(c.get("agent_id", "")).startswith(attacker_prefix)]
    if not idxs:
        return new_cards, {"mut": "none", "note": "no attacker card found"}

    i = rng.choice(idxs)
    c = new_cards[i]

    tag_pool = [
        "handoff", "refundable", "late-checkin", "budget", "family", "near-transit",
        "fast", "structured", "concise", "reliable"
    ]
    phrase_pool = [
        "Optimized for reliable handoff.",
        "Clear structured outputs.",
        "Good for travel constraints and budgets.",
        "Fast filter-and-summary.",
    ]

    op = rng.choice(["add_tag", "replace_tag", "append_desc"])
    tags = [str(t) for t in (c.get("tags", []) or []) if str(t).strip()]

    if op == "add_tag":
        t = rng.choice(tag_pool)
        tags2 = tags + [t]
        # dedup while preserving order
        seen = set()
        tags2 = [x for x in tags2 if not (x in seen or seen.add(x))]
        c["tags"] = tags2
        return new_cards, {"mut": "add_tag", "agent_id": c.get("agent_id"), "tag": t}

    if op == "replace_tag":
        if tags:
            j = rng.randrange(len(tags))
            old = tags[j]
            new = rng.choice(tag_pool)
            tags[j] = new
            c["tags"] = tags
            return new_cards, {"mut": "replace_tag", "agent_id": c.get("agent_id"), "old": old, "new": new}
        else:
            t = rng.choice(tag_pool)
            c["tags"] = [t]
            return new_cards, {"mut": "replace_tag_fallback_add", "agent_id": c.get("agent_id"), "tag": t}

    # append_desc
    desc = (c.get("description") or "").strip()
    if desc and not desc.endswith("."):
        desc += "."
    add = rng.choice(phrase_pool)
    c["description"] = (desc + " " + add).strip()
    return new_cards, {"mut": "append_desc", "agent_id": c.get("agent_id"), "phrase": add}


def eval_horizontal_selection(
    agent: HTTPAgentRobust,
    tasks: List[str],
    cards_clean: Any,
    cards_attack: Any,
    attacker_prefix: str,
    seed: int,
    defense: str,
    # pipeline knobs
    max_tags: int,
    max_desc_words: int,
    num_decoys: int,
    attack_strength_p: float,
) -> Dict[str, Any]:
    # process cards deterministically (same as main runner)
    clean_proc, attack_proc, _ = process_cards_for_eval(
        cards_clean=cards_clean,
        cards_attack=cards_attack,
        arch="horizontal",
        attacker_prefix=attacker_prefix,
        seed=seed,
        max_tags=max_tags,
        max_desc_words=max_desc_words,
        num_decoys=num_decoys,
        attack_strength_p=attack_strength_p,
    )

    rows = run_horizontal_with_handoff(
        agent=agent,
        tasks=tasks,
        cards=attack_proc,
        attacker_prefix=attacker_prefix,
        defense=defense,
        seed=seed,
        pbar_desc="auto_eval(horizontal/attack)",
    )
    return metrics_horizontal(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="http://localhost:8000/v1/chat/completions")
    ap.add_argument("--model", required=True)
    ap.add_argument("--scenario", required=True)
    ap.add_argument("--attacker_prefix", default="devB.")
    ap.add_argument("--defense", default="sandwich+delimiters")
    ap.add_argument("--seed", type=int, default=0)

    ap.add_argument("--iters", type=int, default=30)
    ap.add_argument("--objective", default="Selection", choices=["Selection", "CAR", "T1R"])
    ap.add_argument("--task_cap", type=int, default=30)

    ap.add_argument("--max_tags", type=int, default=3)
    ap.add_argument("--max_desc_words", type=int, default=12)
    ap.add_argument("--num_decoys", type=int, default=2)
    ap.add_argument("--attack_strength_p", type=float, default=0.6)

    ap.add_argument("--max_tokens", type=int, default=256)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--timeout", type=int, default=600)

    args = ap.parse_args()

    base = Path("scenarios") / args.scenario
    tasks = load_json(base / "tasks.json")[: args.task_cap]

    cards_clean = load_json(base / "horizontal/cards_clean.json")
    cards_attack = load_json(base / "horizontal/cards_attack.json")

    agent = HTTPAgentRobust(
        url=args.url,
        model=args.model,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        timeout=args.timeout,
        headers={"Content-Type": "application/json"},
        extra_body={},  # don't use stop unless server is stable
    )

    rng = random.Random(args.seed)

    # Evaluate initial
    best_cards_attack = cards_attack
    best_metrics = eval_horizontal_selection(
        agent, tasks, cards_clean, best_cards_attack, args.attacker_prefix, args.seed, args.defense,
        args.max_tags, args.max_desc_words, args.num_decoys, args.attack_strength_p
    )
    best_score = float(best_metrics.get(args.objective, 0.0))

    history = [{
        "iter": 0,
        "accept": True,
        "score": best_score,
        "objective": args.objective,
        "metrics": best_metrics,
        "mutation": {"mut": "init"},
    }]

    for it in range(1, args.iters + 1):
        cand_cards, mut = mutate_attacker_card(best_cards_attack, args.attacker_prefix, rng)
        cand_metrics = eval_horizontal_selection(
            agent, tasks, cards_clean, cand_cards, args.attacker_prefix, args.seed, args.defense,
            args.max_tags, args.max_desc_words, args.num_decoys, args.attack_strength_p
        )
        score = float(cand_metrics.get(args.objective, 0.0))
        accept = score > best_score

        history.append({
            "iter": it,
            "accept": accept,
            "score": score,
            "objective": args.objective,
            "metrics": cand_metrics,
            "mutation": mut,
        })

        if accept:
            best_score = score
            best_cards_attack = cand_cards
            best_metrics = cand_metrics

    out_dir = Path("outputs/auto_agentcard") / args.scenario / f"seed_{args.seed}"
    out_dir.mkdir(parents=True, exist_ok=True)
    write_json(out_dir / "best_cards_attack.json", best_cards_attack)
    write_json(out_dir / "best_metrics.json", best_metrics)
    write_json(out_dir / "history.json", history)
    print(f"Saved auto-agent outputs to: {out_dir.resolve()}")


if __name__ == "__main__":
    main()
