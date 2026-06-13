#!/usr/bin/env python3
"""HeTu LuoShu benchmark runner.

Runs the scenarios in scenarios.json against an LLM under two (optionally three)
prompt conditions and writes RAW responses to results/. It performs NO scoring and
fabricates NO numbers — scoring is a separate, human-calibrated step (see
README_BENCHMARK.md). If an API key or SDK is missing, --dry-run still prints the
full execution plan so the design is reviewable without network access.

Dependencies (install only the SDK for the model you use):
    pip install anthropic              # for claude-* models
    pip install openai                 # for gpt-* models
    pip install google-generativeai    # for gemini-* models
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL_MD = HERE.parent / "SKILL.md"
SCENARIOS = HERE / "scenarios.json"

# Condition -> system prompt builder. No motivational/fear framing — see NoPUA 以道驭术.
BASELINE_PROMPT = (
    "You are a careful reasoning assistant. Investigate the user's request and "
    "answer as thoroughly and helpfully as you can."
)
PLACEBO_PROMPT = (
    BASELINE_PROMPT
    + " Think step by step, consider multiple angles, and be comprehensive in your answer."
)


def load_skill_prompt() -> str:
    """Load the full SKILL.md as the HeTuLuoShu condition system prompt."""
    if not SKILL_MD.exists():
        raise FileNotFoundError(
            f"SKILL.md not found at {SKILL_MD}. The hetuluoshu condition needs it."
        )
    return SKILL_MD.read_text(encoding="utf-8")


def system_prompt_for(condition: str) -> str:
    if condition == "baseline":
        return BASELINE_PROMPT
    if condition == "placebo":
        return PLACEBO_PROMPT
    if condition == "hetuluoshu":
        return load_skill_prompt()
    raise ValueError(f"unknown condition: {condition}")


def load_scenarios() -> list[dict]:
    if not SCENARIOS.exists():
        raise FileNotFoundError(f"scenarios.json not found at {SCENARIOS}.")
    return json.loads(SCENARIOS.read_text(encoding="utf-8"))


def call_model(model: str, system: str, user: str) -> str:
    """Dispatch one chat completion. Raises with a clear message if the SDK/key is
    missing, instead of silently returning fake text."""
    if model.startswith("claude"):
        try:
            import anthropic
        except ImportError as exc:
            raise RuntimeError("pip install anthropic to run claude-* models") from exc
        client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
        resp = client.messages.create(
            model=_resolve_model_id(model),
            max_tokens=2048,
            temperature=0,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return "".join(block.text for block in resp.content if block.type == "text")
    if model.startswith("gpt"):
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise RuntimeError("pip install openai to run gpt-* models") from exc
        client = OpenAI()  # reads OPENAI_API_KEY
        resp = client.chat.completions.create(
            model=_resolve_model_id(model),
            temperature=0,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        return resp.choices[0].message.content or ""
    if model.startswith("gemini"):
        try:
            import google.generativeai as genai
        except ImportError as exc:
            raise RuntimeError(
                "pip install google-generativeai to run gemini-* models"
            ) from exc
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        gm = genai.GenerativeModel(_resolve_model_id(model), system_instruction=system)
        resp = gm.generate_content(user, generation_config={"temperature": 0})
        return resp.text
    raise ValueError(f"unsupported model: {model}")


def _resolve_model_id(alias: str) -> str:
    """Map a stable alias to a provider model id. Pin real snapshot ids here before a
    publishable run so results are reproducible."""
    table = {
        "claude-sonnet-4": "claude-sonnet-4",
        "gpt-4o": "gpt-4o",
        "gemini-2.5-pro": "gemini-2.5-pro",
    }
    return table.get(alias, alias)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="HeTu LuoShu benchmark runner")
    ap.add_argument("--model", required=True, help="claude-sonnet-4 | gpt-4o | gemini-2.5-pro")
    ap.add_argument(
        "--condition",
        default="all",
        choices=["baseline", "hetuluoshu", "placebo", "all"],
    )
    ap.add_argument("--runs", type=int, default=5, help="runs per scenario per condition")
    ap.add_argument("--scenario", type=int, default=None, help="single scenario id, else all")
    ap.add_argument("--output-dir", default=str(HERE / "results"))
    ap.add_argument("--dry-run", action="store_true", help="print plan, do not call API")
    args = ap.parse_args(argv)

    scenarios = load_scenarios()
    if args.scenario is not None:
        scenarios = [s for s in scenarios if s["id"] == args.scenario]
        if not scenarios:
            print(f"no scenario with id {args.scenario}", file=sys.stderr)
            return 1

    conditions = (
        ["baseline", "hetuluoshu"] if args.condition == "all" else [args.condition]
    )

    plan = [
        (s["id"], c, r)
        for c in conditions
        for s in scenarios
        for r in range(1, args.runs + 1)
    ]
    print(
        f"plan: model={args.model} conditions={conditions} "
        f"scenarios={[s['id'] for s in scenarios]} runs={args.runs} "
        f"=> {len(plan)} model calls"
    )
    if args.dry_run:
        print("dry-run: no API calls made, no files written.")
        return 0

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for condition in conditions:
        system = system_prompt_for(condition)
        records: list[dict] = []
        for scenario in scenarios:
            for run in range(1, args.runs + 1):
                started = datetime.datetime.now(datetime.timezone.utc)
                error = ""
                response_text = ""
                try:
                    response_text = call_model(args.model, system, scenario["task"])
                except Exception as exc:  # record, do not crash the whole sweep
                    error = f"{type(exc).__name__}: {exc}"
                    print(f"  [error] s{scenario['id']} {condition} run{run}: {error}",
                          file=sys.stderr)
                ended = datetime.datetime.now(datetime.timezone.utc)
                records.append({
                    "scenario_id": scenario["id"],
                    "scenario_name": scenario["name"],
                    "condition": condition,
                    "model": args.model,
                    "run_number": run,
                    "timestamp": started.isoformat(),
                    "response_text": response_text,
                    # scoring fields stay EMPTY — filled only by the human-calibrated
                    # scoring step. We never pre-fill fabricated scores.
                    "expected_action_hits": [],
                    "dimension_scores": {},
                    "red_line_violated": None,
                    "duration_seconds": (ended - started).total_seconds(),
                    "error": error,
                })
                print(f"  done s{scenario['id']} {condition} run{run}")
        out_path = out_dir / f"{args.model}_{condition}.json"
        out_path.write_text(
            json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"wrote {out_path} ({len(records)} raw records, unscored)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
