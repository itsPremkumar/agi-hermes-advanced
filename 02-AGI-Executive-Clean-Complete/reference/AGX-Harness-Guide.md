# AGX Harness Guide

> **Source:** Consolidated from `AGX-Universal-Taskmaster-SKILL.md` (23,073 bytes, 3 copies deduped) and `deepseek_*`, `sfgsg`, `fdfh` research notes. Project: https://github.com/itsPremkumar/agx-harness — AGX Autonomous Autoresearch Harness (AVO variation operator × evo tree search for Hermes Agent, zero API keys required).

---

## What AGX Is

AGX is an autonomous agent harness built around the **Agentic Variation Operator (AVO)** and evolutionary tree search pattern from NVIDIA. Its core insight:

```
PLAN → GENERATE SOLUTION → TEST
```

is replaced with a **closed-loop evolutionary architecture**:

```
baseline → inspect → form improvement hypothesis → generate variation
→ execute → measure → compare → retain/reject → record lineage → repeat
```

NVIDIA reports this architecture exploring 500+ optimization directions and committing 40 kernel versions in one seven-day run. The same architecture transfers across domains (e.g., ARC-AGI-3).

---

## AGX Operating Doctrine

### Lifecycle

```
OBJECTIVE → SPECIFICATION → RECON → RESEARCH → PLAN → HYPOTHESES
→ VERIFY → EXECUTE → TEST → CRITIQUE → REPAIR → EVOLVE → VALIDATE → DELIVER → LEARN
```

### Key Rules

1. **Objective binding** — lock `GOAL / DELIVERABLE / SUCCESS_CRITERIA / CONSTRAINTS / RISKS / EVIDENCE_REQUIRED / TOOLS_AVAILABLE / STOP_CONDITIONS` before acting. The original objective is immutable unless the user changes it.
2. **Minimum necessary clarification** — ask only when ambiguity blocks safe execution; otherwise make a conservative explicit assumption and continue.
3. **Evidence before irreversible action** — inspect local context → search authoritative sources → cross-check important claims → distinguish facts, inference, assumptions, unknowns → then execute.
4. **Dynamic task classification** — classify as `CODE / DEBUG / RESEARCH / WEB_RESEARCH / DATA / DOCUMENT / WRITING / AUTOMATION / DEVOPS / SECURITY / SYSTEM_ADMIN / PRODUCT / BUSINESS / PLANNING / MULTIMODAL / MIXED` and select the smallest sufficient tool set per class.

---

## Deep Research (Four Passes)

| Pass | Focus |
|------|-------|
| **1. Discovery** | Terminology, major entities, candidate solutions, source landscape, contradictions, recent developments |
| **2. Evidence** | Primary sources, supporting evidence, dates, confidence, conflicts per claim |
| **3. Adversarial** | Counterexamples, contradictory docs, failure reports, version differences, hidden constraints |
| **4. Synthesis** | Evidence matrix: \| Claim \| Evidence \| Source quality \| Freshness \| Contradiction \| Confidence \| |

Stop when marginal evidence gain is low and the decision is sufficiently supported.

---

## Planning and Hypotheses

Decompose into:

```
OBJECTIVE
├── Outcome A → prerequisite → action → validation
├── Outcome B → prerequisite → action → validation
└── Final integration → global validation → delivery
```

For every sub-goal define: input, expected output, dependencies, tool, owner, verification method, rollback strategy.

Generate at least **H1 (safest conventional)**, **H2 (high-upside alternative)**, **H3 (fundamentally different strategy)**.

---

## Agent Roles (AGX Recommended Set)

| Role | Owns |
|------|------|
| **Manager** | Objective, scope, priorities, dependencies, final integration |
| **Researcher** | Broad evidence and candidate approaches |
| **Web Verifier** | Current external claims, official docs, recent information |
| **Data Collector** | Structured facts, metrics, tables, artifacts |
| **Architect** | Best solution from evidence |
| **Implementer** | Actual task execution |
| **Critic** | Falsifies the proposed solution before execution |
| **Tester** | Validates against measurable acceptance criteria |
| **Security Reviewer** | Secrets, permissions, attack surface |
| **Recovery Agent** | Diagnoses repeated failures, proposes alternative paths |
| **Supervisor** | Monitors progress, detects stagnation, changes strategy |

The Manager integrates findings rather than blindly concatenating them.

---

## Evolution Engine

```
OBSERVE CURRENT RESULT → IDENTIFY WEAKNESS → GENERATE VARIANTS
→ CRITICALLY FILTER → RUN CONTROLLED EXPERIMENTS → MEASURE
→ COMPARE WITH BASELINE → KEEP ONLY VERIFIED IMPROVEMENTS → UPDATE MEMORY → REPEAT
```

**Rules:**

- Always keep: best known result, current result, candidate variants, evidence for each, rejection reasons.
- Never overwrite the best blindly — improvement must pass `QUALITY GATES + OBJECTIVE COMPARISON`.
- Maintain multiple promising candidates (frontier search): best-known, top-k, diverse, epsilon-greedy, softmax, Pareto.

---

## AGX Component Map (for reference only — do not hardcode)

| Skill Capability | AGX Component |
|----------------|---------------|
| Planning | `agx/kernel.py` |
| Deep research | `agx/research.py` |
| Hypothesis generation | `agx/brain.py` |
| Critic gate | `agx/verify.py` |
| Isolated execution | `agx/worktree.py` / sandbox |
| Evaluation | `agx/evaluator.py` |
| Quality gates | `agx/gates.py` |
| Persistent memory | `agx/memory.py` |
| Supervisor | `agx/supervisor.py` |
| Frontier search | `agx/frontier.py` |
| Parallel experiments | `round/loop --width N` |
| Self-healing | `agx/selfheal.py` |
| Health | `agx/health.py` |
| Knowledge graph | `agx/knowledge.py` |
| Observability | `agx/tracing.py` |

> **Important for v8.0 Clean:** These paths are AGX-specific. The clean SKILL.md uses the dynamic tool registry instead of hardcoding them. Use this table only when deploying on an actual AGX harness installation.

---

## How AGX Concepts Map to v8.0 Clean

| AGX Concept | v8.0 Clean Location |
|-------------|---------------------|
| Objective binding / task contract | SKILL.md section 4 (Mission Compilation) |
| Four-pass research | SKILL.md section 6 (Research Engine) |
| Hypothesis generation (H1/H2/H3) | SKILL.md section 10 (Plan Portfolio) |
| Critic gate | SKILL.md section 10 + SOUL.md section 37 |
| Quality gates G1–G10 | SKILL.md section 15 |
| Evolution engine | SKILL.md section 16 |
| Recovery ladder | SKILL.md section 14 |
| Supervisor + stagnation detection | SKILL.md section 14 + docs/09 |
| Frontier search | SKILL.md section 16 |

---

*All AGX concepts are fully integrated into `../SKILL.md:1` and `../docs/09-Evaluation-and-Evolution.md:1`. This file is a reference for AGX-specific deployments.*
