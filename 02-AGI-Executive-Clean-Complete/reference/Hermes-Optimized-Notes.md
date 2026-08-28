# Hermes Optimized Notes

> **Source:** Consolidated from `HERMES-OPTIMIZED-SKILL.md` (42,150 bytes, 2,469 lines) and `files/SKILL.md` / `files (1)/SKILL.md` v7.3 deployment sections. License: MIT. Category: autonomous-ai-agents.

---

## What Hermes Is

Hermes (Nous Research) is a **real, currently deployed, self-hosted autonomous agent runtime** with persistent operation, broad tool access (shell, filesystem, browser, messaging platforms), and long-horizon autonomy. It is not a hypothetical target.

The Hermes skill turns Hermes into a **goal-completion engine, not a conversational planner**:

> Do the actual work required to achieve the user's objective. Do not merely discuss how the work could be done.

---

## Hermes Execution Lifecycle

```
RECEIVE → UNDERSTAND → GOAL CONTRACT → RECON → COMPLEXITY ASSESSMENT
→ DECOMPOSE → DEPENDENCY GRAPH → RESEARCH → COMPETING PLANS
→ SPECIALIST DELEGATION → PARALLEL WORK → COLLECT → EVALUATE
→ BEST-COMPONENT SYNTHESIS → MASTER PLAN → CRITIC GATE
→ EXECUTE → VERIFY → RECOVER / REPLAN WHEN NEEDED → EVOLVE WHEN BENEFICIAL
→ FINAL VERIFICATION → ACCEPTANCE → DELIVER → STOP
```

This is the same canonical loop as `SKILL.md` with Hermes-specific complexity routing.

---

## Complexity-Aware Routing (Hermes Pattern)

Use the smallest sufficient architecture:

| Complexity | Description | Workflow |
|------------|-------------|----------|
| **TRIVIAL** | Single action, known procedure, reversible | Direct execution |
| **MODERATE** | Multiple steps, some unknowns | Plan → Execute → Verify |
| **COMPLEX** | Research required, competing approaches, multi-agent | Full loop with delegation |
| **EXPLORATORY** | Unknown environment, unclear objective | Research → Hypothesis → Experiment → Learn |

Hermes assessments of complexity inform the `Cognitive Router` in `SKILL.md` section 8.

---

## Hermes Frontmatter

```yaml
name: hermes-autonomous-execution
version: 1.0.0
description: >
  Universal goal-driven autonomous execution and orchestration protocol
  optimized for Hermes Agent. Converts substantial user objectives into
  verified, dependency-aware, parallel, evidence-backed execution while
  using Hermes delegation, terminal, file, web, process, skills, memory,
  and related capabilities only when actually available.
author: Autonomous Execution Protocol
license: MIT
metadata:
  hermes:
    tags: [autonomy, orchestration, delegation, research, execution, verification, evolution, recovery]
    category: autonomous-ai-agents
```

---

## Hermes-Specific Guidance

1. **Do not disable Hermes's approval prompts, sandboxing, or credential filtering** in the name of autonomy. Those mechanisms are load-bearing, not friction to optimize away. Independent security research on autonomous agent platforms has documented risks spanning prompt processing, tool use, and memory retrieval.

2. **Terminal backend selection** — pick the most sandboxed backend your setup allows. This is the backend that `SOUL.md` treats as high-blast-radius (R4/R5).

3. **Memory writes** — Hermes defaults to `write_approval: false` (writes freely). The clean `deployment/config.yaml` deliberately sets `write_approval: true` so memory writes go through the same approval discipline as other consequential actions.

4. **Best-component synthesis** — Hermes emphasizes `COLLECT → EVALUATE → BEST-COMPONENT SYNTHESIS → MASTER PLAN` where multiple agents' results are evaluated component-wise and the strongest parts combined, rather than selecting one agent's output wholesale.

---

## How Hermes Concepts Map to v8.0 Clean

| Hermes Concept | v8.0 Clean Location |
|----------------|---------------------|
| Goal contract | SKILL.md section 4 |
| Complexity assessment | SKILL.md section 8 (Cognitive Router) |
| Dependency graph | SKILL.md section 10 (Task Graph) |
| Competing plans | SKILL.md section 10 (Plan Portfolio) |
| Specialist delegation | SKILL.md section 11 + docs/06 |
| Best-component synthesis | SKILL.md section 11 (Parallel Experimentation) |
| Critic gate | SKILL.md section 10, docs/08 |
| Evolution when beneficial | SKILL.md section 16 |
| Deployment config | `../deployment/config.yaml:1` |

---

*All Hermes concepts are fully integrated into `../SKILL.md:1`. This file is a reference for Hermes-specific deployments.*
