#!/usr/bin/env python3
"""Validate the CSL Claude plugin marketplace.

Checks
  1. marketplace.json: required fields, every plugin source exists, names unique,
     dependencies resolve to plugins in this marketplace.
  2. plugin.json: present, name matches folder and marketplace entry, versions agree.
  3. SKILL.md: YAML frontmatter, name matches folder, description length
     (error above 1,024 characters, warning above 900).
  4. Every file named in a skill's "Files in this skill" section exists.
  5. Commands and agents have frontmatter with a description.
  6. Cross-references to csl-* skills resolve to a skill in this repository.
  7. Policy lint: no references to the retired AGENT.md or config/ files, no
     single-user personalization, no credentials, no emojis.
  8. Python files compile.

Exit code 1 on any error. Run from the repository root:  python3 scripts/validate.py
"""
from __future__ import annotations

import json
import py_compile
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []
warnings: list[str] = []

# Files allowed to mention retired names because they document the migration.
MIGRATION_DOCS = {"MIGRATION.md", "REVIEW.md", "CHANGELOG.md", "connector-map.md", "validate.py", "csl-operating-rules/SKILL.md"}

RETIRED = [
    (re.compile(r"AGENT\.md"), "reference to retired AGENT.md; cite csl-operating-rules"),
    (re.compile(r"config/(user-profile|client-context|tool-registry)"), "reference to retired config/ file; cite the engagement context file or connector map"),
    (re.compile(r"\bEsteban\b"), "single-user personalization"),
]
SECRET = re.compile(r"(?i)(api[_-]?key|secret|password|bearer)\s*[:=]\s*['\"][A-Za-z0-9_\-]{12,}['\"]")
EMOJI = re.compile("[\U0001F300-\U0001FAFF\u2600-\u26FF\u2700-\u27BF]")
BRAND_TOKENS = {f"csl-{c}" for c in ("red", "black", "white", "navy", "teal", "teal-dark", "olive", "ink", "slate", "grey", "mist", "paper")}
FRONT = re.compile(r"^---\n(.*?)\n---\n", re.S)


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    m = FRONT.match(text)
    if not m:
        err(f"{rel(path)}: missing YAML frontmatter")
        return {}
    fm: dict[str, str] = {}
    key = None
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if km:
            key = km.group(1)
            val = km.group(2).strip()
            fm[key] = "" if val in (">", "|", ">-", "|-") else val.strip('"')
        elif key and line.startswith("  "):
            fm[key] = (fm[key] + " " + line.strip()).strip()
    return fm


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


def main() -> int:
    mp_path = ROOT / ".claude-plugin" / "marketplace.json"
    if not mp_path.exists():
        err(".claude-plugin/marketplace.json missing")
        return report()
    mp = json.loads(mp_path.read_text())
    for f in ("name", "owner", "plugins"):
        if f not in mp:
            err(f"marketplace.json missing '{f}'")
    names = [p["name"] for p in mp.get("plugins", [])]
    if len(names) != len(set(names)):
        err("marketplace.json has duplicate plugin names")

    all_skills: set[str] = set()
    plugin_dirs = []
    for entry in mp.get("plugins", []):
        src = ROOT / entry["source"]
        if not src.is_dir():
            err(f"plugin '{entry['name']}' source {entry['source']} not found")
            continue
        plugin_dirs.append((entry, src))
        for dep in entry.get("dependencies", []):
            if dep.split("@")[0] not in names:
                err(f"plugin '{entry['name']}' depends on unknown plugin '{dep}'")
        pj_path = src / ".claude-plugin" / "plugin.json"
        if not pj_path.exists():
            err(f"{rel(src)}: plugin.json missing")
            continue
        pj = json.loads(pj_path.read_text())
        if pj.get("name") != entry["name"] or src.name != entry["name"]:
            err(f"{rel(pj_path)}: name '{pj.get('name')}' does not match folder/entry '{entry['name']}'")
        if entry.get("version") and pj.get("version") and entry["version"] != pj["version"]:
            warn(f"{entry['name']}: marketplace version differs from plugin.json")
        for s in (src / "skills").glob("*/SKILL.md"):
            all_skills.add(s.parent.name)

    for entry, src in plugin_dirs:
        for skill_md in sorted((src / "skills").glob("*/SKILL.md")):
            check_skill(skill_md, all_skills)
        for kind in ("commands", "agents"):
            for md in sorted((src / kind).glob("*.md")):
                fm = frontmatter(md)
                if not fm.get("description"):
                    err(f"{rel(md)}: frontmatter needs a description")
                check_refs(md, all_skills)

    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix in {".md", ".py", ".json", ".html", ".css", ".yml"}:
            lint(path)
        if path.suffix == ".py":
            try:
                py_compile.compile(str(path), doraise=True)
            except py_compile.PyCompileError as e:
                err(f"{rel(path)}: does not compile: {e.msg.splitlines()[0]}")
    return report()


def check_skill(skill_md: Path, all_skills: set[str]) -> None:
    folder = skill_md.parent
    fm = frontmatter(skill_md)
    if fm.get("name") != folder.name:
        err(f"{rel(skill_md)}: name '{fm.get('name')}' does not match folder '{folder.name}'")
    desc = fm.get("description", "")
    if not desc:
        err(f"{rel(skill_md)}: description missing")
    elif len(desc) > 1024:
        err(f"{rel(skill_md)}: description {len(desc)} chars exceeds 1,024")
    elif len(desc) > 900:
        warn(f"{rel(skill_md)}: description {len(desc)} chars; target is 900")
    text = skill_md.read_text(encoding="utf-8")
    lines = text.count("\n")
    if lines > 500:
        warn(f"{rel(skill_md)}: {lines} lines; consider moving detail to references/")
    m = re.search(r"^## Files in this skill.*?$(.*)", text, re.S | re.M)
    if m:
        for ref in re.findall(r"`((?:references|templates|scripts|assets)/[^`\s]+)`", m.group(1)):
            if "*" in ref or "<" in ref:
                continue
            if not (folder / ref).exists():
                err(f"{rel(skill_md)}: lists missing file {ref}")
    check_refs(skill_md, all_skills)


def check_refs(path: Path, all_skills: set[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for name in set(re.findall(r"`(csl-[a-z0-9-]+)`", text)):
        if name not in all_skills and not name.startswith(("csl-core", "csl-project-delivery", "csl-business-development")):
            if name == "csl-meeting-minutes" or name in BRAND_TOKENS:
                continue  # legacy renderer (companion skill) or a csl-brand CSS token
            warn(f"{rel(path)}: references unknown skill `{name}`")


def lint(path: Path) -> None:
    r = rel(path)
    allowed = any(r.endswith(m) for m in MIGRATION_DOCS)
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not allowed:
        for rx, msg in RETIRED:
            for mm in rx.finditer(text):
                line = text.count("\n", 0, mm.start()) + 1
                err(f"{r}:{line}: {msg}")
    if SECRET.search(text):
        err(f"{r}: looks like a credential")
    if path.suffix == ".md" and EMOJI.search(text):
        warn(f"{r}: contains an emoji (CSL style: none)")


def report() -> int:
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
