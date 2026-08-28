# HERMES Advanced — Hermes-Native Executive System

**Version:** 2.0 Advanced (Hermes-Native) + SOUL v4.0 ASI + AGENTS.md  
**Type:** Professional Hermes-Native Build — Advanced, Clean, Official-Compliant  
**Hermes Runtime:** Hermes Agent (Nous Research) — https://hermes-agent.nousresearch.com  
**Language:** English Only — Professional Standard

---

## What This Is

**THE dedicated Hermes folder** — built FOR Hermes, ON Hermes, WITH Hermes. Every file is Hermes-native and follows the **official Hermes standard** (`hermes-agent.nousresearch.com/docs`).

```
05-HERMES-Advanced/                    ← This folder — THE Hermes system (Professional)
│
├── SOUL.md (48KB, 50 sections)        ← Hermes identity — WHO Hermes is (slot #1 in system prompt)
├── AGENTS.md (project context)        ← Project rules — what applies ONLY to this Hermes project
├── SKILL.md (18KB, 15 planes)         ← Hermes Advanced OS — HOW Hermes works
├── config.yaml                        ← Single Hermes config (official: ~/.hermes/config.yaml)
├── .env.example                       ← Secrets template (official: ~/.hermes/.env)
├── MEMORY.md (4.0 chars)              ← Persistent memory (official: ~/.hermes/MEMORY.md)
├── USER.md  (2.0 chars)               ← User profile (official: ~/.hermes/USER.md)
│
├── skills/ (8 Hermes-native skills)   ← Official: skills/<category>/<skill>/SKILL.md
│   ├── 01-research/SKILL.md           ← 5-pass research + Evidence Graph
│   ├── 02-planning/SKILL.md           ← 6 plans + DAG + 10 strategies
│   ├── 03-orchestration/SKILL.md      ← Swarm + 30 roles + Debate Protocol
│   ├── 04-tools/SKILL.md              ← Tool Registry + Computer-Use + Sandbox
│   ├── 05-safety-evaluation/SKILL.md  ← R0-R6 + 22 Invariants + 12 Gates
│   ├── 06-memory-world/SKILL.md       ← World Model + 15 Namespaces + Context OS
│   ├── 07-search-optimized/SKILL.md   ← Flagship: Search Superintelligence
│   └── 08-project-synthesis/SKILL.md  ← NEW: Project Synthesis Engine (reuse/modify/combine/scratch)
│       └── templates/                 ← Evidence templates (official: skill templates/)
│           ├── evidence-graph.md
│           ├── sources.md
│           └── contradictions.md
│
└── docs/ (2 Essential Guides)         ← Professional: only important docs
    ├── 02-Architecture.md             ← 15-plane architecture deep dive
    └── 06-Search-Optimization.md      ← Flagship: How Hermes search works
```

**Total:** 20 professional files — every file is important per Hermes, no clutter.

---

## Why Professional Now?

| Before (Unwanted) | After (Professional, per Official Hermes) | Why |
|---|---|---|
| `AGENT.md` (singular, non-standard) | `AGENTS.md` (official project context) | Official: `AGENTS.md` is project rules, `SOUL.md` is global identity |
| `config/` + `config.search.yaml` + `config.production.yaml` (3 configs) | `config.yaml` (single, official) | Official: one `~/.hermes/config.yaml` — profiles are documented as comments inside it |
| `memory/MEMORY.md` (subfolder) | `MEMORY.md` at root (official) | Official: `~/.hermes/MEMORY.md` is at home root, not subfolder |
| `deployment/install.ps1` + `install.sh` | Removed (use `hermes setup`) | Official: `hermes setup` and `hermes skills install` are the installers |
| `evidence/template/` (top-level) | `skills/07-search-optimized/templates/` (per skill) | Official: skill templates belong in `skills/<skill>/templates/` |
| `examples/` (3 files) | Removed (in SKILL.md procedure) | Official: examples belong in SKILL.md `## Procedure` and `## Pitfalls` |
| `docs/` 9 files | `docs/` 2 files (Architecture + Search) | Professional: only flagship docs; common info is in SKILL.md via progressive disclosure |
| `README.md` 151 lines with old structure diagram | Updated to new professional structure | Professional: reflects the cleaned, official-compliant layout |

**Removed 14 files** — kept only what is **important per Hermes official docs**.

---

## Hermes Official File Map

| File in This Folder | Installs To (Official Hermes Location) | Purpose |
|---|---|---|
| `SOUL.md` | `~/.hermes/SOUL.md` | Global identity — slot #1 in system prompt |
| `AGENTS.md` | `~/.hermes/skills/hermes-advanced/AGENTS.md` or project `AGENTS.md` | Project-only rules |
| `SKILL.md` | `~/.hermes/skills/hermes-advanced/SKILL.md` | Hermes Advanced OS |
| `skills/07-search-optimized/SKILL.md` | `~/.hermes/skills/hermes-search-optimized/SKILL.md` | Search flagship skill |
| `config.yaml` | `~/.hermes/config.yaml` | Settings (model, terminal, memory, toolsets) |
| `.env.example` | `~/.hermes/.env` | Secrets (fill API keys) |
| `MEMORY.md` | `~/.hermes/MEMORY.md` | Persistent facts |
| `USER.md` | `~/.hermes/USER.md` | User preferences |

---

## Quick Start — Official Hermes Way

```bash
# 1. Install (official)
hermes setup                          # Interactive setup — creates ~/.hermes/config.yaml + .env
# Or manually:
cp config.yaml ~/.hermes/config.yaml
cp .env.example ~/.hermes/.env        # Edit: add ANTHROPIC_API_KEY
cp SOUL.md ~/.hermes/SOUL.md
cp MEMORY.md ~/.hermes/MEMORY.md
cp USER.md ~/.hermes/USER.md
cp -r skills/* ~/.hermes/skills/

# 2. Configure
hermes config set model anthropic/claude-sonnet-4
hermes config set terminal.backend docker
hermes tools                          # Enable web_search, browser, file_*

# 3. Verify (search flagship test)
hermes chat -q "Search the live web for 'Hermes Agent Nous Research latest release 2026' and cite primary source with date — use parallel searches and browser extraction"

# Expected: 3-5 parallel web_search → browser load top 3 → evidence graph in templates/ → report with citations
```

---

## The Three Files Hermes Loads Every Task (Official)

| File | Role (Official Hermes) | When |
|------|------------------------|------|
| `SOUL.md` | WHO Hermes is — identity, voice, boundaries — **slot #1 in system prompt** | **Every task** |
| `AGENTS.md` | Project context — conventions, ports, workflows — **project-only** | **When in this project** |
| `SKILL.md` + `skills/*` | HOW Hermes works — 15 planes, swarm, search — **progressive disclosure** | **On demand** (router picks 1-3) |

---

## Advanced Highlights — Still High-Level

- **15-Plane Architecture** — Strategic Superintelligence + Formal Verification + Self-Evolution (see `docs/02-Architecture.md`)
- **Hermes Search Superintelligence** — 5 parallel `web_search` + browser + evidence graph + contradiction + second wave (see `docs/06-Search-Optimization.md` and `skills/07-search-optimized/`)
- **Hermes Swarm** — 30+ roles, 3-5 parallel workers, best-component synthesis, debate protocol (`skills/03-orchestration/`)
- **R0-R6 Risk + 22 Invariants + 12 Gates** — ASI-grade safety (`skills/05-safety-evaluation/`)
- **Official-Compliant Skill Frontmatter** — `requires_tools: [web_search]`, `requires_toolsets: [web]`, `metadata.hermes` per `hermes-agent.nousresearch.com/docs/developer-guide/creating-skills`
- **Skill Templates** — Evidence templates in `skills/07-search-optimized/templates/` per official `skills/<category>/<skill>/templates/` structure

---

## Docs — Read in Order (Professional, Minimal)

1.  `docs/02-Architecture.md` — 15 planes deep dive (the system)
2.  `docs/06-Search-Optimization.md` — Flagship: How Hermes search works (the superpower)

Common workflows are in `SKILL.md` via **progressive disclosure** (official guideline: most common first, edge cases at bottom) — not in separate docs.

---

*HERMES Advanced v2.0 Professional — Built FOR Hermes per official Hermes docs (hermes-agent.nousresearch.com).*
*15 planes, 7 skills, 1 SOUL, 1 AGENTS, 1 config, 2 memory files — every file is important per Hermes, no clutter.*
*From 34 files → 20 professional files. Advanced, clean, official-compliant.*
