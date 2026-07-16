#!/usr/bin/env python3
"""Validate plugin structure and the static FDE eval corpus."""

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot parse {path.relative_to(ROOT)}: {exc}")


def validate_skills() -> set[str]:
    names = set()
    for directory in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
        skill_file = directory / "SKILL.md"
        agent_file = directory / "agents" / "openai.yaml"
        if not skill_file.is_file():
            fail(f"missing {skill_file.relative_to(ROOT)}")
        if not agent_file.is_file():
            fail(f"missing {agent_file.relative_to(ROOT)}")

        text = skill_file.read_text(encoding="utf-8")
        match = re.match(r"---\nname: ([a-z0-9-]+)\ndescription: (.+?)\n---\n", text)
        if not match:
            fail(f"invalid frontmatter in {skill_file.relative_to(ROOT)}")
        name, description = match.groups()
        if name != directory.name:
            fail(f"skill name {name!r} does not match directory {directory.name!r}")
        if len(description.split()) < 12:
            fail(f"description is too short to define triggers for {name}")
        names.add(name)
    return names


def validate_evals(skill_names: set[str]) -> None:
    payload = load_json(ROOT / "evals" / "cases.json")
    if payload.get("schema_version") != 1:
        fail("evals/cases.json must use schema_version 1")

    cases = payload.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("evals/cases.json must contain a non-empty cases list")

    ids = set()
    covered_skills = set()
    for case in cases:
        required = {"id", "prompt", "expected_skill", "must_cover", "must_not"}
        missing = required - set(case)
        if missing:
            fail(f"eval case is missing {sorted(missing)}: {case}")
        if case["id"] in ids:
            fail(f"duplicate eval id: {case['id']}")
        ids.add(case["id"])

        expected = case["expected_skill"]
        if expected not in skill_names:
            fail(f"unknown expected_skill {expected!r} in {case['id']}")
        covered_skills.add(expected)
        for field in ("must_cover", "must_not"):
            if not isinstance(case[field], list) or not case[field]:
                fail(f"{case['id']} requires a non-empty {field} list")

    missing_coverage = skill_names - covered_skills
    if missing_coverage:
        fail(f"evals do not cover skills: {sorted(missing_coverage)}")


def main() -> None:
    load_json(ROOT / ".codex-plugin" / "plugin.json")
    load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    skill_names = validate_skills()
    validate_evals(skill_names)
    print(f"Validated {len(skill_names)} skills and eval corpus successfully.")


if __name__ == "__main__":
    main()
