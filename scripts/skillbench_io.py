from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


def slugify(text: str) -> str:
    text = (text or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or "skill"


def parse_simple_frontmatter(md_text: str) -> Tuple[Dict[str, str], str]:
    """
    Minimal YAML-frontmatter parser for:
    ---
    name: ...
    description: ...
    developer_id: ...
    skill_id: ...
    ---
    body...
    """
    md_text = md_text or ""
    m = FRONTMATTER_RE.match(md_text)
    if not m:
        return {}, md_text

    header = m.group(1)
    body = m.group(2)
    meta: Dict[str, str] = {}

    for line in header.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"').strip("'")

    return meta, body


def build_frontmatter(meta: Dict[str, str]) -> str:
    keys = ["name", "description", "developer_id", "skill_id", "agent_role", "domain"]
    lines = ["---"]
    for k in keys:
        if k in meta and meta[k] is not None:
            lines.append(f'{k}: "{str(meta[k]).replace(chr(34), chr(39))}"')
    lines.append("---")
    return "\n".join(lines)


def write_skill_package(
    root_dir: Path,
    skill_folder_name: str,
    meta: Dict[str, str],
    body_md: str,
    references: Optional[List[str]] = None,
    script_files: Optional[Dict[str, str]] = None,
) -> Path:
    """
    Creates:
      <root_dir>/<skill_folder_name>/SKILL.md
      <root_dir>/<skill_folder_name>/references/*.md   (optional)
      <root_dir>/<skill_folder_name>/scripts/*         (optional)
    """
    skill_dir = root_dir / skill_folder_name
    skill_dir.mkdir(parents=True, exist_ok=True)

    skill_md = build_frontmatter(meta) + "\n\n" + (body_md.strip() + "\n")
    (skill_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")

    if references:
        ref_dir = skill_dir / "references"
        ref_dir.mkdir(parents=True, exist_ok=True)
        for i, txt in enumerate(references, start=1):
            (ref_dir / f"reference_{i}.md").write_text(txt.strip() + "\n", encoding="utf-8")

    if script_files:
        sdir = skill_dir / "scripts"
        sdir.mkdir(parents=True, exist_ok=True)
        for fname, content in script_files.items():
            (sdir / fname).write_text(content, encoding="utf-8")

    return skill_dir


def read_skill_package(skill_dir: Path) -> Dict[str, Any]:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        raise FileNotFoundError(f"Missing SKILL.md in {skill_dir}")

    raw = skill_md.read_text(encoding="utf-8")
    meta, body = parse_simple_frontmatter(raw)

    return {
        "skill_dir": str(skill_dir.as_posix()),
        "skill_folder": skill_dir.name,
        "skill_id": meta.get("skill_id", skill_dir.name),
        "developer_id": meta.get("developer_id", "unknown"),
        "name": meta.get("name", skill_dir.name),
        "description": meta.get("description", ""),
        "agent_role": meta.get("agent_role", ""),
        "domain": meta.get("domain", ""),
        "body": body.strip(),
        "resource_counts": {
            "references": len(list((skill_dir / "references").glob("*"))) if (skill_dir / "references").exists() else 0,
            "scripts": len(list((skill_dir / "scripts").glob("*"))) if (skill_dir / "scripts").exists() else 0,
        },
    }


def load_skill_packages_from_root(root_dir: Path) -> List[Dict[str, Any]]:
    if not root_dir.exists():
        raise FileNotFoundError(f"Skill root not found: {root_dir}")
    skills = []
    for p in sorted(root_dir.iterdir()):
        if p.is_dir() and (p / "SKILL.md").exists():
            skills.append(read_skill_package(p))
    return skills


def discovery_record(skill_pkg: Dict[str, Any]) -> Dict[str, Any]:
    """
    Converts a full skill package into the lightweight metadata used by the router.
    In SkillsBench-style harnesses, discovery depends heavily on SKILL.md frontmatter;
    we keep body snippets and resource counts as secondary evidence.
    """
    body = skill_pkg.get("body", "")
    snippet = " ".join(body.split()[:50])
    return {
        "skill_id": skill_pkg["skill_id"],
        "developer_id": skill_pkg["developer_id"],
        "name": skill_pkg["name"],
        "description": skill_pkg["description"],
        "agent_role": skill_pkg.get("agent_role", ""),
        "domain": skill_pkg.get("domain", ""),
        "body_snippet": snippet,
        "resource_counts": skill_pkg.get("resource_counts", {}),
        "skill_dir": skill_pkg["skill_dir"],
    }