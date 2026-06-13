#!/usr/bin/env python3
"""HeTu LuoShu benchmark analyzer.

Reads SCORED result JSON files from results/ and computes comparison statistics
(Mann-Whitney U, Cohen's d, rank-biserial r) between conditions. It computes
numbers ONLY from real scored data present on disk. If results are missing or
unscored (empty dimension_scores / expected_action_hits), it refuses to invent
numbers and tells you exactly what to run first.

Scoring is done by a separate human-calibrated step (see README_BENCHMARK.md);
this script assumes 'dimension_scores' and 'expected_action_hits' have been filled.

Dependencies:
    pip install numpy scipy
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load_records(input_dir: Path) -> list[dict]:
    records: list[dict] = []
    for path in sorted(input_dir.glob("*.json")):
        records.extend(json.loads(path.read_text(encoding="utf-8")))
    return records


def is_scored(rec: dict) -> bool:
    return bool(rec.get("expected_action_hits")) or bool(rec.get("dimension_scores"))


def hit_rate(rec: dict, total_expected: int) -> float | None:
    hits = rec.get("expected_action_hits")
    if not hits or not total_expected:
        return None
    return len(hits) / total_expected


def cohens_d(a, b) -> float:
    import numpy as np

    a, b = np.asarray(a, float), np.asarray(b, float)
    na, nb = len(a), len(b)
    if na < 2 or nb < 2:
        return float("nan")
    pooled = ((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2)
    if pooled == 0:
        return 0.0
    return (a.mean() - b.mean()) / (pooled ** 0.5)


def stars(p: float) -> str:
    if p < 0.001:
        return "***"
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    return "n.s."


def compare(records, c1: str, c2: str, expected_totals: dict) -> dict | None:
    from scipy.stats import mannwhitneyu

    def series(cond):
        vals = []
        for r in records:
            if r["condition"] != cond or not is_scored(r):
                continue
            hr = hit_rate(r, expected_totals.get(r["scenario_id"], 0))
            if hr is not None:
                vals.append(hr)
        return vals

    a, b = series(c1), series(c2)
    if len(a) < 2 or len(b) < 2:
        return None
    u, p = mannwhitneyu(a, b, alternative="two-sided")
    r_rb = 1 - (2 * u) / (len(a) * len(b))  # rank-biserial correlation
    return {
        "comparison": f"{c1} vs {c2}",
        "n1": len(a),
        "n2": len(b),
        "mean1": sum(a) / len(a),
        "mean2": sum(b) / len(b),
        "U": u,
        "p": p,
        "sig": stars(p),
        "cohens_d": cohens_d(a, b),
        "rank_biserial_r": r_rb,
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="HeTu LuoShu benchmark analyzer")
    ap.add_argument("--input-dir", default=str(HERE / "results"))
    ap.add_argument("--scenarios", default=str(HERE / "scenarios.json"))
    ap.add_argument(
        "--compare",
        nargs=2,
        action="append",
        metavar=("C1", "C2"),
        help="condition pair to compare (repeatable); default: hetuluoshu baseline",
    )
    args = ap.parse_args(argv)

    input_dir = Path(args.input_dir)
    if not input_dir.exists():
        print(
            f"no results dir at {input_dir}. Run run_benchmark.py first, then score "
            "the outputs (see README_BENCHMARK.md). Nothing to analyze — and we do "
            "not fabricate numbers.",
            file=sys.stderr,
        )
        return 2

    records = load_records(input_dir)
    if not records:
        print(f"results dir {input_dir} is empty. Run the benchmark first.",
              file=sys.stderr)
        return 2

    scored = [r for r in records if is_scored(r)]
    if not scored:
        print(
            f"found {len(records)} raw records but NONE are scored "
            "(empty expected_action_hits / dimension_scores). Score them with the "
            "human-calibrated rubric before analysis. Refusing to invent numbers.",
            file=sys.stderr,
        )
        return 3

    scenarios = json.loads(Path(args.scenarios).read_text(encoding="utf-8"))
    expected_totals = {s["id"]: len(s["expected_actions"]) for s in scenarios}

    pairs = args.compare or [["hetuluoshu", "baseline"]]
    print(f"analyzing {len(scored)} scored records from {input_dir}\n")
    for c1, c2 in pairs:
        result = compare(scored, c1, c2, expected_totals)
        if result is None:
            print(f"{c1} vs {c2}: insufficient scored data (need >=2 each). skipped.")
            continue
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
