#!/usr/bin/env python3
"""
test_skills_schema.py — Pytest validation suite for Hermes ASI Master skills
Validates YAML frontmatter, official Hermes metadata, required files, and helper scripts.
"""

import os
import pathlib
import pytest
import yaml
import ast

WORKSPACE_ROOT = pathlib.Path(__file__).parent.parent
HERMES_DIR = WORKSPACE_ROOT / "05-HERMES-Advanced"
SKILLS_DIR = HERMES_DIR / "skills"

def get_skill_files():
    """Finds all SKILL.md files in 05-HERMES-Advanced/skills/."""
    assert SKILLS_DIR.exists(), f"Skills directory not found at {SKILLS_DIR}"
    skills = list(SKILLS_DIR.glob("*/SKILL.md"))
    return skills

def parse_frontmatter(content: str):
    """Extracts and parses YAML frontmatter from markdown text."""
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    raw_yaml = parts[1]
    return yaml.safe_load(raw_yaml)

def test_core_identity_files():
    """Verify that core identity, memory, and config files exist and are populated."""
    core_files = ["SOUL.md", "AGENTS.md", "MEMORY.md", "USER.md", "config.yaml", ".env.example", "mcp_servers.json"]
    for filename in core_files:
        filepath = HERMES_DIR / filename
        assert filepath.exists(), f"Required core file missing: {filepath}"
        assert filepath.stat().st_size > 0, f"Core file is empty: {filepath}"

def test_config_yaml_syntax():
    """Verify that config.yaml is valid YAML."""
    config_path = HERMES_DIR / "config.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    assert isinstance(data, dict), "config.yaml must parse to a dictionary"

def test_skill_count():
    """Ensure all 12 modular skills are present."""
    skills = get_skill_files()
    assert len(skills) >= 12, f"Expected at least 12 skills, found {len(skills)}"

@pytest.mark.parametrize("skill_path", get_skill_files(), ids=lambda p: p.parent.name)
def test_skill_frontmatter(skill_path: pathlib.Path):
    """Verify that each SKILL.md has valid frontmatter matching Hermes standards."""
    text = skill_path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    assert fm is not None, f"Missing or malformed YAML frontmatter in {skill_path}"
    assert "name" in fm, f"Frontmatter missing 'name' field in {skill_path}"
    assert "description" in fm, f"Frontmatter missing 'description' field in {skill_path}"
    assert len(fm["description"]) > 10, f"Description is too short in {skill_path}"

def test_python_helper_syntax():
    """Verify all Python scripts in the workspace have valid Python syntax."""
    py_files = list(WORKSPACE_ROOT.glob("**/*.py"))
    for py_file in py_files:
        if ".gemini" in str(py_file) or ".git" in str(py_file):
            continue
        code = py_file.read_text(encoding="utf-8")
        try:
            ast.parse(code, filename=str(py_file))
        except SyntaxError as e:
            pytest.fail(f"Syntax error in {py_file}: {e}")
