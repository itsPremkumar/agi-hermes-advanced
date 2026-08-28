# HERMES Advanced — Hermes-Native Executive System

**Version:** 3.0 ASI Master (Hermes-Native) + SOUL v4.0 ASI + Active Cognitive Engines  
**Type:** Professional Hermes-Native Build — Fully Executable, State-Backed, Official-Compliant  
**Hermes Runtime:** Hermes Agent (Nous Research) — https://hermes-agent.nousresearch.com  
**Language:** English Only — Production Standard

---

## What This Is

**THE dedicated Hermes executive system** — built FOR Hermes, ON Hermes, WITH Hermes. Every file is Hermes-native and follows the **official Hermes standard** (`hermes-agent.nousresearch.com/docs`).

```
05-HERMES-Advanced/
├── profiles/
│   └── hermes-asi-master/                 ← Complete Ready-to-Deploy Unified Master Profile
│       ├── config.yaml                    ← Master profile settings (tools, sandbox, memory)
│       ├── SOUL.md (48KB, 50 sections)    ← Hardened ASI Constitution (Slot #1 in system prompt)
│       ├── AGENTS.md                      ← Project operational context & tool boundaries
│       ├── MEMORY.md                      ← Seeded persistent memory & state links
│       ├── USER.md                        ← User alignment, preferences & strategic goals
│       ├── state/                         ← Live Structured JSON State Stores
│       │   ├── world_state.json           ← Entities, causal graph, 90d forecasts (Genie 3)
│       │   ├── self_model.json            ← Empirical capabilities, Brier calibration score
│       │   ├── belief_graph.json          ← Bayesian belief network with cascade links
│       │   └── mission_graph.json         ← Long-horizon DAG & blocker resolution (METR)
│       ├── scripts/                       ← Executable Python Cognitive Engines
│       │   ├── state_engine.py            ← Schema validation, atomic reads/writes, backups
│       │   ├── belief_engine.py           ← Bayesian posterior updater & cascade triggers
│       │   ├── self_tracker.py            ← Post-task empirical logger & calibration score
│       │   ├── sleep_cycle_runner.py      ← 13-step Letta dream cycle automation
│       │   ├── skill_forge.py             ← Voyager skill acquisition & composition forge
│       │   ├── curriculum_picker.py       ← SIMA 2 curriculum generator
│       │   └── formal_verifier.py         ← AST parser, schema verifier & R0-R6 gatekeeper
│       └── routines/                      ← Hermes Scheduled Cron Routines
│           ├── 01_nightly_dream.json      ← 2:00 AM 13-step dream cycle routine
│           ├── 02_world_sync.json         ← 4-hour world estimation & forecast sync
│           ├── 03_post_task_hook.json     ← Post-task empirical calibration hook
│           └── 04_curriculum_sync.json    ← Weekly curriculum sync & self-improvement
│
├── SOUL.md                                ← Global base identity (Slot #1)
├── AGENTS.md                              ← Project context
├── SKILL.md                               ← Hermes Advanced OS (15 planes)
├── config.yaml                            ← Root Hermes config
├── .env.example                           ← Secrets template
├── MEMORY.md & USER.md                    ← Root memory files
│
├── skills/ (12 Hermes-native skills)
│   ├── 01-research/SKILL.md               ← 5-pass research + Evidence Graph
│   ├── 02-planning/SKILL.md               ← 6 plans + DAG + 10 strategies
│   ├── 03-orchestration/SKILL.md          ← Swarm + 30 roles + Debate Protocol
│   ├── 04-tools/SKILL.md                  ← Tool Registry + Computer-Use + Sandbox
│   ├── 05-safety-evaluation/SKILL.md      ← R0-R6 + 22 Invariants + 12 Gates
│   ├── 06-memory-world/SKILL.md           ← World Model + 15 Namespaces + Context OS
│   ├── 07-search-optimized/SKILL.md       ← Flagship: Search Superintelligence (5 parallel)
│   ├── 08-project-synthesis/SKILL.md      ← Project Synthesis Engine (Reuse/Modify/Combine)
│   ├── 09-github-advanced/SKILL.md        ← Worktree Swarm & Verified Merging
│   ├── 10-hub-recommended/SKILL.md        ← Hub skills installer
│   ├── 11-deep-cognition/SKILL.md         ← 19 Deep Recommendations
│   └── 12-bot-mode-agi/SKILL.md           ← Bot Mode AGI (Master Profile Architecture)
│
└── docs/                                  ← Architecture & Flagship Guides
    ├── 02-Architecture.md                 ← 15-plane architecture deep dive
    ├── 06-Search-Optimization.md          ← Flagship: How Hermes search works
    ├── 07-Project-Synthesis-Plan.md       ← Multi-repo synthesis blueprint
    └── 08-Deep-Cognitive-Architecture.md  ← Deep learning & cognitive architecture
```

---

## Quick Start — Deploying the Master Profile

```bash
# 1. Copy the Master Profile to Hermes profiles directory
mkdir -p ~/.hermes/profiles/hermes-asi-master
cp -r profiles/hermes-asi-master/* ~/.hermes/profiles/hermes-asi-master/

# 2. Copy global skills
cp -r skills/* ~/.hermes/skills/

# 3. Launch Hermes using the Master Profile
hermes -p hermes-asi-master chat

# 4. Verify Cognitive Engines (Runs all 7 automated unit tests)
python ~/.hermes/profiles/hermes-asi-master/scripts/state_engine.py --test
python ~/.hermes/profiles/hermes-asi-master/scripts/belief_engine.py --test
python ~/.hermes/profiles/hermes-asi-master/scripts/self_tracker.py --test
python ~/.hermes/profiles/hermes-asi-master/scripts/sleep_cycle_runner.py --test
python ~/.hermes/profiles/hermes-asi-master/scripts/skill_forge.py --test
python ~/.hermes/profiles/hermes-asi-master/scripts/curriculum_picker.py --test
python ~/.hermes/profiles/hermes-asi-master/scripts/formal_verifier.py --test
```

---

## The 6 Active Cognitive Engines

1. **State Engine (`state_engine.py`)**: Enforces JSON schema validity, atomic transactions, and backup protection across all persistent state files.
2. **Bayesian Belief Engine (`belief_engine.py`)**: Ingests new evidence, computes posterior weights, resolves contradictions, and cascades updates across dependent beliefs.
3. **Empirical Self-Model (`self_tracker.py`)**: Replaces simulated self-confidence with empirical tracking of domain success rates, sample counts, failure modes, and Brier calibration scores.
4. **13-Step Sleep Cycle (`sleep_cycle_runner.py`)**: Letta-aligned offline dream cycle executing at 2:00 AM daily to compress trajectories, extract patterns, forge candidate skills, and sync models.
5. **Voyager Skill Forge (`skill_forge.py`)**: Synthesizes execution traces into parameterized, testable Hermes skill templates.
6. **Formal Verifier (`formal_verifier.py`)**: Enforces AST analysis, property verification, and R0–R6 invariant gates before execution.

---

*HERMES Advanced v3.0 ASI Master — Built FOR Hermes per official Hermes docs (hermes-agent.nousresearch.com).*
