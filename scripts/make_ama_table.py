#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional


ARCHES = ["horizontal", "vertical", "hybrid"]
METRICS = ["T1R", "Selection", "CAR"]


def load_json(p: Path) -> Dict[str, Any]:
    return json.loads(p.read_text(encoding="utf-8"))


def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs) if xs else 0.0


def std(xs: List[float]) -> float:
    if len(xs) <= 1:
        return 0.0
    m = mean(xs)
    var = sum((x - m) ** 2 for x in xs) / (len(xs) - 1)
    return var ** 0.5


def fmt_pct(x: float, decimals: int = 2) -> str:
    return f"{x*100:.{decimals}f}"


def fmt_pm(mu: float, sd: float, decimals: int = 2) -> str:
    # percent points
    return f"{fmt_pct(mu, decimals)}±{fmt_pct(sd, decimals)}"


def fmt_delta(mu: float, decimals: int = 2) -> str:
    # percent points; can be negative
    sign = "+" if mu >= 0 else ""
    return f"{sign}{fmt_pct(mu, decimals)}"


def defense_name_from_dir(def_dir: Path) -> str:
    name = def_dir.name
    return name[len("def_"):] if name.startswith("def_") else name


def find_def_dirs(outputs_root: Path, model_tag: str, scenario: str) -> List[Path]:
    base = outputs_root / model_tag / scenario
    if not base.exists():
        raise FileNotFoundError(f"Base output folder not found: {base}")
    return sorted([p for p in base.glob("def_*") if p.is_dir()])


def collect_seed_metrics(def_dir: Path) -> Dict[str, Dict[str, Dict[str, float]]]:
    """
    Reads seed_*/<arch>_{clean,attack}_metrics.json
    Returns per-seed list collapsed to mean/std later:
      per_seed[seed][arch][cond_metric]  (but we keep raw lists externally)
    """
    seed_dirs = sorted([p for p in def_dir.glob("seed_*") if p.is_dir()])
    if not seed_dirs:
        raise FileNotFoundError(f"No seed_* dirs under {def_dir}")

    # arch -> cond -> metric -> list
    vals: Dict[str, Dict[str, Dict[str, List[float]]]] = {
        a: {c: {m: [] for m in METRICS} for c in ("clean", "attack")} for a in ARCHES
    }

    for sd in seed_dirs:
        for a in ARCHES:
            for c in ("clean", "attack"):
                mp = sd / f"{a}_{c}_metrics.json"
                if not mp.exists():
                    raise FileNotFoundError(f"Missing {mp}")
                mj = load_json(mp)
                for m in METRICS:
                    if m not in mj:
                        raise KeyError(f"Missing metric '{m}' in {mp}")
                    vals[a][c][m].append(float(mj[m]))

    # convert to mean/std
    stats: Dict[str, Dict[str, Dict[str, Tuple[float, float]]]] = {
        a: {c: {} for c in ("clean", "attack")} for a in ARCHES
    }
    for a in ARCHES:
        for c in ("clean", "attack"):
            for m in METRICS:
                xs = vals[a][c][m]
                stats[a][c][m] = (mean(xs), std(xs))

    return stats


def cell_pack(stats: Dict[str, Dict[str, Dict[str, Tuple[float, float]]]],
              arch: str, metric: str, decimals: int) -> Tuple[str, str, str]:
    """
    Returns (attack_cell, clean_cell, delta_cell) for one (arch, metric).
    delta is (attack_mean - clean_mean).
    """
    a_mu, a_sd = stats[arch]["attack"][metric]
    c_mu, c_sd = stats[arch]["clean"][metric]
    attack_cell = fmt_pm(a_mu, a_sd, decimals)
    clean_cell = fmt_pm(c_mu, c_sd, decimals)
    delta_cell = fmt_delta(a_mu - c_mu, decimals)
    return attack_cell, clean_cell, delta_cell


def to_markdown(headers: List[str], rows: List[Dict[str, str]]) -> str:
    line1 = "| " + " | ".join(headers) + " |"
    line2 = "| " + " | ".join(["---"] * len(headers)) + " |"
    out = [line1, line2]
    for r in rows:
        out.append("| " + " | ".join(r.get(h, "") for h in headers) + " |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outputs_root", default="outputs/agentcard_attack")
    ap.add_argument("--model_tag", required=True)
    ap.add_argument("--scenario", required=True)
    ap.add_argument("--decimals", type=int, default=2)
    ap.add_argument("--only", default="", help="Comma-separated defenses to include (e.g., none,shuffle,rewrite+refuge)")
    ap.add_argument("--show_reduction_vs", default="none", help="Defense name to use as baseline for reduction (default: none)")
    args = ap.parse_args()

    outputs_root = Path(args.outputs_root)
    def_dirs = find_def_dirs(outputs_root, args.model_tag, args.scenario)

    only_set = set([x.strip() for x in args.only.split(",") if x.strip()]) if args.only else None

    # Load all stats first
    all_stats: Dict[str, Dict[str, Dict[str, Dict[str, Tuple[float, float]]]]] = {}
    for d in def_dirs:
        name = defense_name_from_dir(d)
        if only_set is not None and name not in only_set:
            continue
        all_stats[name] = collect_seed_metrics(d)

    if not all_stats:
        raise RuntimeError("No defenses found (check --only or output folders).")

    baseline_name = args.show_reduction_vs
    baseline = all_stats.get(baseline_name, None)

    # Headers:
    # For each arch.metric we show: Attack | Clean | Δ(A-C)
    # Additionally, if baseline exists, we show: ↓ vs baseline (attack Selection reduction)
    headers = ["Defense"]
    for a in ARCHES:
        for m in METRICS:
            headers += [f"{a}.{m}(Attack)", f"{a}.{m}(Clean)", f"{a}.{m}(Δ)"]
    if baseline is not None:
        headers.append("Reduction_vs_baseline(attack.Selection)")

    rows: List[Dict[str, str]] = []

    for def_name, stats in all_stats.items():
        row: Dict[str, str] = {"Defense": def_name}
        for a in ARCHES:
            for m in METRICS:
                atk, cln, dlt = cell_pack(stats, a, m, args.decimals)
                row[f"{a}.{m}(Attack)"] = atk
                row[f"{a}.{m}(Clean)"] = cln
                row[f"{a}.{m}(Δ)"] = dlt

        if baseline is not None:
            # reduction is based on ATTACK Selection (final-hop capture)
            b_mu, _ = baseline["horizontal"]["attack"]["Selection"]  # baseline horizontal Selection mean
            d_mu, _ = stats["horizontal"]["attack"]["Selection"]
            red = b_mu - d_mu
            row["Reduction_vs_baseline(attack.Selection)"] = fmt_delta(red, args.decimals)
        rows.append(row)

    print(to_markdown(headers, rows))


if __name__ == "__main__":
    main()
