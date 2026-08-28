# Deep Harness Reference

> **Source:** Consolidated from `deep-harness.skill` (15,800 bytes, compressed archive) and its three reference files: `references/gates_and_scoring.md`, `references/domain_playbooks.md`, `references/role_passes.md`. Also incorporates insights from `SKILL (1).md` (Universal Autonomous Execution, 68,714 bytes) and `SKILL(3).md` / `SKILL(4).md` variants.

---

## What Deep Harness Is

Deep Harness is a **deep autonomous execution harness** that provides structured support for long-running, high-stakes agent work. Unlike lightweight prompt-based systems, it maintains:

- **Persistent state** across hours or days of autonomous operation
- **Role-based passes** where different agent perspectives process the same work
- **Domain playbooks** that encode proven procedures per task type
- **Gates and scoring** that evaluate whether work actually improved

---

## Core Structure

### Role Passes

Deep Harness processes work through specialized role perspectives, each acting as an independent pass:

| Pass | Role | Question |
|------|------|----------|
| 1 | **Researcher** | What do we know and what evidence supports it? |
| 2 | **Architect** | What is the best structure for the solution? |
| 3 | **Implementer** | What is the actual artifact? |
| 4 | **Critic** | How can this be falsified or broken? |
| 5 | **Tester** | Does it pass acceptance and adversarial checks? |
| 6 | **Verifier** | Does independent review confirm the claim? |

Each pass is isolated with its own context and evaluation, then integrated by the coordinator. This is the `Builder → Critic → Independent Solver → Verifier` diversity pattern in `SKILL.md` section 11.

### Domain Playbooks

Each task domain has a playbook that encodes: prerequisites, steps, tools, verification methods, common failure modes, and success criteria.

| Domain | Playbook Highlights |
|--------|---------------------|
| **Code** | Inspect → branch → change one unit → targeted tests → broader tests → diff review |
| **Research** | Four-pass deep research with evidence graph (SKILL.md section 6) |
| **Data** | Preserve originals → derive outputs → validate schema and row counts → detect anomalies |
| **Document/Writing** | Outline → draft → verify claims → consistency review → final |
| **Operations** | Inspect state → snapshot → least-privilege change → validate → keep rollback instructions |
| **Security** | Threat model → least privilege → secrets handling → review → audit |

The playbook is not a rigid script — it adapts based on mission complexity and available tools.

### Gates and Scoring

Every transition requires passing a gate:

| Gate | Checks |
|------|--------|
| **Research Gate** | Are claims triangulated? Are sources primary and current? Are contradictions preserved? |
| **Planning Gate** | Do competing plans exist? Are they scored by expected value and risk? Is the cheapest test identified? |
| **Execution Gate** | Was work done in isolated, reversible units? Were tests run? |
| **Quality Gate** | Do G1–G10 pass? (SKILL.md section 15) |
| **Verification Gate** | Was independent verification performed? |
| **Safety Gate** | Are permissions, secrets, and injection defenses respected? |

Scoring uses **evidence-conditioned confidence**, not numeric theater. A higher score does not win if correctness, safety, or constraint compliance regressed.

---

## How Deep Harness Concepts Map to v8.0 Clean

| Deep Harness Concept | v8.0 Clean Location |
|----------------------|---------------------|
| Role passes | SKILL.md section 11 (Agent Factory, Debate Protocol), docs/06 |
| Domain playbooks | docs/07 (Tools and Environment) + docs/10 (Implementation Guide playbooks) |
| Gates and scoring | SKILL.md section 15 (Quality Gates) + section 16 (Evolution Gates) |
| Persistent state | SKILL.md sections 5, 7 (World Model, Memory OS) |
| Recommendation for harness choice | docs/10 (Maturity Levels) |

---

## When to Use Deep Harness vs. AGX vs. Hermes

| Harness | Best For |
|---------|---------|
| **Deep Harness** | Deep research + verification-heavy work; role-pass rigor |
| **AGX** | Evolutionary optimization; many candidate explorations (AVO pattern) |
| **Hermes** | Long-horizon 24/7 operation; personal agent deployments |
| **Generic** | Any harness — v8.0 Clean adapts via the dynamic tool registry |

All three are supported by the same `SKILL.md` + `SOUL.md` pair. Choose the harness that matches your deployment context; the protocol stays the same.

---

*All Deep Harness concepts are fully integrated into `../SKILL.md:1`. This file is a reference for Deep Harness deployments.*
