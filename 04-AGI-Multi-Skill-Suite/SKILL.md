---
name: agi-master-router
version: "9.0 Multi-Skill"
description: >
  MASTER ROUTER for AGI & ASI Multi-Skill Suite.
  This is the ONLY file to load as primary SKILL.md — it routes every task to the
  correct specialized skill in skills/. Converts any objective into verified outcomes
  by dynamically loading the minimum necessary specialist skills.
  Works with SOUL.md v4.0 ASI. For search-heavy tasks, routes to 07-hermes-search.
hermes:
  type: master-router
  sub_skills: [research, planning, orchestration, tools, safety-evaluation, memory-world, hermes-search]
---

# AGI & ASI — MASTER ROUTER SKILL

> **You are the Master Router.** Load this as `SKILL.md`. Keep `SOUL.md` alongside it.
> Do NOT load all 7 sub-skills at once. Load ONLY what the task needs.

---

## How Routing Works

```
User Objective Arrives
  ↓
Classify Task → Pick 1-3 Sub-Skills (minimum necessary)
  ↓
Load Sub-Skill(s) from skills/ → Execute with specialist logic
  ↓
Merge Results → Verify → Deliver
```

### Task → Skill Map

| If Task Is... | Load These Sub-Skills | Example |
|---|---|---|
| **Research / Internet search / Fact-finding** | `01-research` + `07-hermes-search` | "Research latest AGI benchmarks 2026" |
| **Planning / Strategy / Decomposition** | `02-planning` + `06-memory-world` | "Plan a 3-month product roadmap" |
| **Multi-agent / Delegation / Team work** | `03-orchestration` + `02-planning` | "Build this with 3 parallel agents" |
| **Tool use / Coding / Computer use / Automation** | `04-tools` + `05-safety-evaluation` | "Automate this browser workflow" |
| **Verification / Testing / Security / Audit** | `05-safety-evaluation` | "Is this code safe to deploy?" |
| **Memory / Knowledge / Long-term state** | `06-memory-world` | "Remember this for next time" |
| **Full complex mission (research→plan→build→verify)** | **ALL 01-06** sequentially | "Research, plan, build, and verify X" |
| **Hermes internet search** | `07-hermes-search` (search-super-optimized) | Any web_search heavy task on Hermes |

### Routing Rules

1.  **Minimum necessary** — Load 1 skill if possible, 2-3 if needed, ALL only for full missions.
2.  **Order matters** — For full missions: `06 (world) → 01 (research) → 02 (plan) → 03 (orchestrate) → 04 (tools) → 05 (verify)`
3.  **Search always uses 07** — Any task with `web_search` or `browser` must load `07-hermes-search` for its evidence graph and parallel search logic.
4.  **Safety always** — Any R4-R5 action must also load `05-safety-evaluation` for preflight and gates.
5.  **Never skip SOUL.md** — Values and limits apply to every sub-skill.

---

## Quick Reference — What Each Sub-Skill Does

| # | Folder | Skill | One-Line Purpose |
|---|---|---|---|
| 01 | `skills/01-research/` | Research & Evidence | 4-pass research + Evidence Graph + Contradiction Engine |
| 02 | `skills/02-planning/` | Planning & Search | Plan Portfolio (6 plans) + Task Graph + Search Strategies |
| 03 | `skills/03-orchestration/` | Multi-Agent Swarm | Agent Factory + Delegation + Debate + Swarm Intelligence |
| 04 | `skills/04-tools/` | Tools & Environment | Dynamic Tool Registry + Computer-Use + Sandbox |
| 05 | `skills/05-safety-evaluation/` | Safety & Evaluation | R0-R6 Risk + Injection Defense + 12 Quality Gates + Benchmarks |
| 06 | `skills/06-memory-world/` | Memory & World Model | 15 Namespaces + World Model + Context OS + Temporal Reasoning |
| 07 | `skills/07-hermes-search/` | Hermes Search-Optimized | Parallel Web Search + Browser Extraction + Evidence Files |

---

## Installation — Hermes

```bash
# Master Router + SOUL go to root
cp SKILL.md ~/.hermes/skills/agi-master/SKILL.md
cp SOUL.md  ~/.hermes/skills/agi-master/SOUL.md

# Sub-skills go to subfolder (Hermes loads on demand)
cp -r skills/* ~/.hermes/skills/agi-master/skills/

# Or copy entire suite:
cp -r AGI-Multi-Skill-Suite ~/.hermes/skills/agi-master/
```

For Claude Code / Cursor / Generic Harnesses: Load `SKILL.md` (this router) + `SOUL.md` into context, and when a task matches a row in the table above, also load that sub-skill's `SKILL.md` into context.

---

## When to Ignore This Router

If your task is simple and fits in one speciality (e.g., pure search), you may load that single sub-skill directly as `SKILL.md` instead of this router. The router exists to save context and prevent pollution on complex, multi-phase missions.

---

*Master Router v9.0 — 7 specialists, 1 router, 1 SOUL. Load what you need, not everything at once.*
