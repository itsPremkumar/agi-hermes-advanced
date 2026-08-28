# AGI Multi-Skill Suite — 7 Specialized Skills + Master Router

**Version:** 9.0 Multi-Skill (Built from AGI & ASI Ultimate v9.0)  
**Structure:** 1 Master Router `SKILL.md` + 1 Shared `SOUL.md` + 7 Specialist `skills/*/SKILL.md`  
**Language:** English Only — Clean, Modular, Production-Ready  
**For:** Hermes, OpenClaw, AGX, Claude Code, Cursor — any harness that supports multi-skill loading

---

## Why Multiple Skills?

Your original project had 40 files with duplicated SKILLs. Your `AGI-ASI-Ultimate` solved that with 1 perfect `SKILL.md` + 1 `SOUL.md`. This **Multi-Skill Suite** solves the NEXT problem:

> **"One giant SKILL.md wastes context on every task."**

If Hermes loads a 52KB SKILL for a simple web search, 80% of that context is irrelevant planning/orchestration text that pollutes reasoning. **Multi-skill fixes this:**

```
Single Skill (before): Load 52KB for EVERY task → context pollution
Multi-Skill (now):     Load 5-15KB specialist for EACH task → clean, fast, precise
```

**Token savings:** ~70% per task. **Quality gain:** Specialist logic is undiluted.

---

## Structure

```
AGI-Multi-Skill-Suite/
│
├── SKILL.md                          ← MASTER ROUTER (load this as primary SKILL.md)
├── SOUL.md                           ← Shared constitution (load always, from Ultimate v4.0 ASI)
├── SKILL-ULTIMATE-BACKUP.md          ← Backup of the single-file Ultimate (if you need it)
│
└── skills/
    ├── 01-research/SKILL.md          ← Research & Evidence Synthesis (5-pass, Evidence Graph)
    ├── 02-planning/SKILL.md          ← Planning & Search (6 plans, DAG, 10 search strategies)
    ├── 03-orchestration/SKILL.md     ← Multi-Agent Swarm (30+ roles, Delegation, Debate)
    ├── 04-tools/SKILL.md             ← Tools & Environment (Registry, Computer-Use, Sandbox)
    ├── 05-safety-evaluation/SKILL.md ← Safety & Evaluation (R0-R6, 22 Invariants, 12 Gates)
    ├── 06-memory-world/SKILL.md      ← Memory & World Model (15 Namespaces, Bayesian Epistemics)
    └── 07-hermes-search/SKILL.md     ← Hermes Search-Optimized (Parallel Web Search, Browser)
```

**Total:** 9 files (1 router + 1 SOUL + 7 specialists). Each specialist is 5-14KB, focused, load-on-demand.

---

## Which Skill Does What?

| # | Skill | When to Load | Size | Load With |
|---|-------|--------------|------|-----------|
| 01 | **Research** | Any fact-finding, source verification | ~8 KB | +07 for live web |
| 02 | **Planning** | Goal decomposition, plan selection, search | ~7 KB | +06 for world state |
| 03 | **Orchestration** | Multi-agent, delegation, swarm | ~9 KB | +02 for task graph |
| 04 | **Tools** | Tool use, browser, computer-use, sandbox | ~7 KB | +05 for safety |
| 05 | **Safety & Evaluation** | Risk, security, verification, evolution | ~10 KB | Always for R4-R6 |
| 06 | **Memory & World** | World model, memory, context, epistemics | ~9 KB | First in full missions |
| 07 | **Hermes Search** | Hermes internet search (live web_search+browser) | ~13 KB | +01 for research logic |
| — | **Master Router** | **Full missions (research→plan→build→verify)** | ~4 KB | Routes to 01-07 |

---

## How to Use

### Option A — Hermes (Recommended for Search Tasks)

```bash
# Install entire suite
cp -r AGI-Multi-Skill-Suite ~/.hermes/skills/agi-suite/

# Hermes loads Master Router as primary
# Master Router dynamically loads specialists per task:
#   "Research X" → loads 01 + 07
#   "Plan and build Y" → loads 06 → 01 → 02 → 03 → 04 → 05
```

### Option B — Claude Code / Cursor / Generic

```
Load in context:
  1. SOUL.md (always)
  2. SKILL.md (Master Router — this file)
  3. When task matches table above, ALSO load that specialist's SKILL.md

Example for "Research latest Hermes docs and plan deployment":
  Load: SOUL.md + Master Router + 06-memory-world + 01-research + 07-hermes-search + 02-planning
```

### Option C — Single-Skill Fallback

If your harness does NOT support multi-skill loading, use the backup:

```bash
cp SKILL-ULTIMATE-BACKUP.md ~/.hermes/skills/agi-suite/SKILL.md  # 52KB single file
cp SOUL.md ~/.hermes/skills/agi-suite/SOUL.md
```

You lose the 70% token savings but keep all capabilities.

---

## Task → Skill Routing Examples

**Example 1: "Search the web for Hermes Agent best practices 2026"**
```
Load: SOUL.md + Master Router + 01-research + 07-hermes-search
Flow: Query compile → 5 parallel searches → Triage → Browser extract → Evidence graph → Report
```

**Example 2: "Plan a multi-agent build for this feature"**
```
Load: SOUL.md + Master Router + 06-memory-world + 02-planning + 03-orchestration
Flow: World model → Mission compile → 6-plan portfolio → DAG → Delegation → Swarm execution
```

**Example 3: "Full mission: Research, plan, build, and verify feature X"**
```
Load: SOUL.md + Master Router + 06 → 01+07 → 02 → 03 → 04 → 05 (sequentially)
Flow: Complete operating loop from AGI-ASI-Ultimate, but each phase uses its specialist
```

**Example 4: "Is this code safe to deploy?"**
```
Load: SOUL.md + Master Router + 05-safety-evaluation
Flow: Risk tier (R0-R6) → Preflight → Injection check → 12 gates → Formal verification → Report
```

---

## Comparison

| Suite | Files | Primary Use | Best For |
|-------|-------|-------------|----------|
| `AGI-ASI-Ultimate` (2 files) | `SKILL.md` + `SOUL.md` | Single-file simplicity | Harnesses that load one SKILL.md |
| **`AGI-Multi-Skill-Suite` (9 files)** | **Router + SOUL + 7 specialists** | **Modular, on-demand loading** | **Hermes, multi-skill harnesses, token-sensitive deployments** |
| `AGI-Executive-Clean-Complete` (24 files) | SKILL + SOUL + 10 docs + refs | Full documentation | Learning, reference, audit |

All three suites contain **100% of the same ultimate logic** — they differ only in how it is packaged. Pick one.

---

## Verification

```bash
ls -R AGI-Multi-Skill-Suite/skills/
# Should show 7 SKILL.md files:

# 01-research, 02-planning, 03-orchestration, 04-tools,
# 05-safety-evaluation, 06-memory-world, 07-hermes-search

cat AGI-Multi-Skill-Suite/SKILL.md | head -20
# Should show: name: agi-master-router
```

All 7 specialists are derived from `SKILL.md` v9.0 ASI (Ultimate) — no concept lost, just split for efficiency.

---

*AGI Multi-Skill Suite v9.0 — 7 specialists, 1 router, 1 SOUL. Load what you need, not everything at once.*
*Built from 42 source files → Ultimate 2-file → Modular 7-skill. English only. Production-ready.*
