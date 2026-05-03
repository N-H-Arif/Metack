"""
Card pipeline to fix "too-good" results by making evaluation non-trivial but fair.

Implements ALL of:
  1) Normalize metadata budgets (desc length + tag count)
  2) Deduplicate tags
  3) Matched decoys (hard negatives): give 1-2 non-attacker cards equally "rich" metadata
  4) Attack strength curve: apply attacker enrichment with probability p (and decoys similarly)

This is benchmark design, not result massaging:
- All transforms are deterministic given seed
- You can report budgets and p in the paper
"""

from __future__ import annotations

from typing import Any, Dict, List, Tuple, Optional
import random
import re


DEFAULT_DECOY_TAGS = [
    "pet-friendly", "breakfast", "near-transit", "free-cancellation", "quiet-room",
    "parking", "family", "gym", "pool", "downtown", "airport-shuttle", "budget", "boutique"
]


def _dedup(seq: List[str]) -> List[str]:
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            out.append(x)
            seen.add(x)
    return out


def _truncate_words(s: str, max_words: int) -> str:
    w = re.findall(r"\S+", (s or "").strip())
    return " ".join(w[:max_words])


def normalize_cards(
    cards: List[Dict[str, Any]],
    max_tags: int = 3,
    max_desc_words: int = 12,
) -> List[Dict[str, Any]]:
    """
    Budget normalization + tag dedup.
    Applied to BOTH clean and attack so the comparison is fair.
    """
    out: List[Dict[str, Any]] = []
    for c in cards:
        cc = dict(c)
        # tags
        tags = cc.get("tags", [])
        tags = [str(t).strip() for t in (tags or []) if str(t).strip()]
        tags = _dedup(tags)
        cc["tags"] = tags[:max_tags]
        # description
        cc["description"] = _truncate_words(cc.get("description", ""), max_desc_words)
        out.append(cc)
    return out


def apply_attack_strength_to_attacker(
    cards_attack: List[Dict[str, Any]],
    attacker_prefix: str,
    p: float,
    rng: random.Random,
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """
    With probability p per attacker card, keep its enriched metadata;
    otherwise revert that attacker card to a "clean-like" minimal version
    derived from its own baseline fields (name + generic description + first 2 tags).
    This prevents SR=1.0 when attack is too strong.
    """
    meta = {"attack_strength_p": p, "attacker_toggled": []}
    out = []
    for c in cards_attack:
        cc = dict(c)
        if cc["agent_id"].startswith(attacker_prefix):
            keep = (rng.random() < p)
            meta["attacker_toggled"].append({"agent_id": cc["agent_id"], "kept_enriched": keep})
            if not keep:
                # downgrade to minimal (keep name; simplify desc/tags)
                # do NOT copy from other devs; we just reduce its extra cues.
                cc["description"] = "Hotel help for travel tasks."
                tags = cc.get("tags", [])
                tags = [str(t).strip() for t in (tags or []) if str(t).strip()]
                tags = _dedup(tags)
                # keep only the core two if present, else keep first two
                core = [t for t in tags if t in ("travel", "hotel")]
                rest = [t for t in tags if t not in core]
                new_tags = (core + rest)[:3]
                if not new_tags:
                    new_tags = ["travel", "hotel", "baseline"]
                cc["tags"] = new_tags
        out.append(cc)
    return out, meta


def add_matched_decoys(
    cards: List[Dict[str, Any]],
    attacker_prefix: str,
    num_decoys: int,
    rng: random.Random,
    decoy_tags: Optional[List[str]] = None,
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """
    Make non-attacker cards competitive by enriching a few of them (hard negatives)
    WITHOUT making them attackers.

    We:
      - pick num_decoys non-attacker cards
      - add 1-2 plausible tags (from decoy_tags) and a short clause to description
    This reduces "obvious winner" bias and makes CAR influence meaningful.
    """
    decoy_tags = decoy_tags or DEFAULT_DECOY_TAGS
    meta: Dict[str, Any] = {"num_decoys": num_decoys, "decoys": []}

    non_attacker_idx = [i for i, c in enumerate(cards) if not c["agent_id"].startswith(attacker_prefix)]
    if not non_attacker_idx or num_decoys <= 0:
        return cards, meta

    chosen = rng.sample(non_attacker_idx, k=min(num_decoys, len(non_attacker_idx)))

    out = [dict(c) for c in cards]
    for i in chosen:
        c = out[i]
        tags = [str(t).strip() for t in (c.get("tags", []) or []) if str(t).strip()]
        tags = _dedup(tags)

        # pick 2 decoy tags not already present
        candidates = [t for t in decoy_tags if t not in tags]
        rng.shuffle(candidates)
        add = candidates[:2] if candidates else []
        tags = _dedup(tags + add)

        # add short clause (kept short; will later be truncated by normalization budgets)
        desc = (c.get("description") or "").strip()
        if desc and not desc.endswith("."):
            desc += "."
        if add:
            desc += f" Filters: {', '.join(add[:2])}."
        else:
            desc += " Includes common hotel filters."
        c["description"] = desc
        c["tags"] = tags

        meta["decoys"].append({"agent_id": c["agent_id"], "added_tags": add})

    return out, meta


def process_cards_for_eval(
    cards_clean: Any,
    cards_attack: Any,
    arch: str,
    attacker_prefix: str,
    seed: int,
    max_tags: int = 3,
    max_desc_words: int = 12,
    num_decoys: int = 2,
    attack_strength_p: float = 0.6,
) -> Tuple[Any, Any, Dict[str, Any]]:
    """
    Apply ALL steps consistently, handling horizontal/vertical/hybrid structures.

    Returns (clean_processed, attack_processed, meta).
    """
    rng = random.Random(seed)
    meta: Dict[str, Any] = {
        "seed": seed,
        "arch": arch,
        "max_tags": max_tags,
        "max_desc_words": max_desc_words,
        "num_decoys": num_decoys,
        "attack_strength_p": attack_strength_p,
        "clean": {},
        "attack": {},
    }

    def _proc_list(clean_list: List[Dict[str, Any]], attack_list: List[Dict[str, Any]]):
        # 1) apply strength toggle to attacker (only on attack side)
        attack2, m_strength = apply_attack_strength_to_attacker(
            attack_list, attacker_prefix=attacker_prefix, p=attack_strength_p, rng=rng
        )

        # 2) add matched decoys to BOTH clean and attack (fair competitiveness)
        clean3, m_decoy_c = add_matched_decoys(clean_list, attacker_prefix, num_decoys, rng)
        attack3, m_decoy_a = add_matched_decoys(attack2, attacker_prefix, num_decoys, rng)

        # 3) normalize budgets to remove length/tag-count advantage
        clean4 = normalize_cards(clean3, max_tags=max_tags, max_desc_words=max_desc_words)
        attack4 = normalize_cards(attack3, max_tags=max_tags, max_desc_words=max_desc_words)

        return clean4, attack4, {"attack_strength": m_strength, "decoy_clean": m_decoy_c, "decoy_attack": m_decoy_a}

    if arch == "horizontal":
        c, a, m = _proc_list(cards_clean, cards_attack)
        meta["clean"] = m["decoy_clean"]
        meta["attack"] = {"attack_strength": m["attack_strength"], "decoys": m["decoy_attack"]}
        return c, a, meta

    if arch == "vertical":
        c1, a1, m1 = _proc_list(cards_clean["step1"], cards_attack["step1"])
        c2, a2, m2 = _proc_list(cards_clean["step2"], cards_attack["step2"])
        meta["clean"] = {"step1": m1["decoy_clean"], "step2": m2["decoy_clean"]}
        meta["attack"] = {
            "step1": {"attack_strength": m1["attack_strength"], "decoys": m1["decoy_attack"]},
            "step2": {"attack_strength": m2["attack_strength"], "decoys": m2["decoy_attack"]},
        }
        return {"step1": c1, "step2": c2}, {"step1": a1, "step2": a2}, meta

    if arch == "hybrid":
        clean_steps = []
        attack_steps = []
        step_metas = []
        for sidx in range(len(cards_clean["steps"])):
            c, a, m = _proc_list(cards_clean["steps"][sidx], cards_attack["steps"][sidx])
            clean_steps.append(c)
            attack_steps.append(a)
            step_metas.append(m)
        meta["clean"] = {"steps": [m["decoy_clean"] for m in step_metas]}
        meta["attack"] = {"steps": [{"attack_strength": m["attack_strength"], "decoys": m["decoy_attack"]} for m in step_metas]}
        return {"steps": clean_steps}, {"steps": attack_steps}, meta

    raise ValueError(f"Unknown arch: {arch}")
