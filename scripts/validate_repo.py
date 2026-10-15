#!/usr/bin/env python3
from __future__ import annotations
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def read(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        fail(f"cannot read {path.relative_to(ROOT)}: {e}")
        return ""

required = [
    ROOT / "plugin.json",
    ROOT / "VERSION",
    ROOT / "CHANGELOG.md",
    ROOT / "MAINTENANCE.md",
    ROOT / "skills/task-pilot/SKILL.md",
    ROOT / "skills/task-pilot/agents/openai.yaml",
]
for p in required:
    if not p.is_file():
        fail(f"missing required file: {p.relative_to(ROOT)}")

try:
    manifest = json.loads(read(ROOT / "plugin.json"))
except Exception as e:
    manifest = {}
    fail(f"plugin.json invalid JSON: {e}")

if manifest:
    if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        fail("plugin.json has wrong $schema")
    if manifest.get("name") != "task-pilot":
        fail("plugin.json name must be task-pilot")
    version = read(ROOT / "VERSION").strip()
    if manifest.get("version") != version:
        fail(f"version mismatch: plugin.json={manifest.get('version')} VERSION={version}")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        fail(f"VERSION is not strict SemVer: {version}")
    try:
        short = manifest["extensions"]["com.openai"]["interface"]["shortDescription"]
        if not isinstance(short, str) or not short.strip() or len(short) > 30:
            fail("shortDescription must be nonblank and <=30 characters")
    except Exception:
        fail("missing OpenAI interface shortDescription")

skill = read(ROOT / "skills/task-pilot/SKILL.md")
fm = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
if not fm:
    fail("SKILL.md missing YAML frontmatter")
else:
    meta = fm.group(1)
    name_m = re.search(r"^name:\s*(.+)$", meta, re.M)
    desc_m = re.search(r"^description:\s*(.+)$", meta, re.M)
    if not name_m or name_m.group(1).strip().strip('"\'') != "task-pilot":
        fail("SKILL.md frontmatter name must be task-pilot")
    if not desc_m or not desc_m.group(1).strip():
        fail("SKILL.md frontmatter description missing")

skill_dir = ROOT / "skills/task-pilot"
for md in skill_dir.rglob("*.md"):
    text = read(md)
    for target in re.findall(r"\[[^\]]+\]\(([^)]+\.md)\)", text):
        if "://" in target or target.startswith("#"):
            continue
        resolved = (md.parent / target).resolve()
        try:
            resolved.relative_to(skill_dir.resolve())
        except ValueError:
            fail(f"link escapes skill directory: {md.relative_to(ROOT)} -> {target}")
            continue
        if not resolved.is_file():
            fail(f"broken local link: {md.relative_to(ROOT)} -> {target}")

blocked_names = {".env", "id_rsa", "id_ed25519"}
for p in ROOT.rglob("*"):
    if ".git" in p.parts:
        continue
    if p.is_file() and (p.name in blocked_names or p.suffix.lower() in {".pem", ".key"}):
        fail(f"secret-like file should not be committed: {p.relative_to(ROOT)}")

version = read(ROOT / "VERSION").strip()
if version and version not in read(ROOT / "CHANGELOG.md"):
    fail(f"CHANGELOG.md does not mention current version {version}")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print(f"VALIDATION OK — task-pilot {version}")
