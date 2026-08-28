---
name: agi-planning-search
version: "9.0"
parent: agi-master-router
scope: Mission Compilation, Goal Decomposition, Planning, Search, Replanning
planes: [Mission, Planning, Strategic Superintelligence]
---

# SKILL 02 — PLANNING & SEARCH

> **Load this skill when:** Task needs goal decomposition, task graphs, plan selection, or search over strategies.
> **Requires:** Mission context + World Model from 06-memory-world (load 06 first if world state is stale).

---

## 1. Mission Compilation

Every mission becomes a durable object:

```yaml
mission:
  id: unique_id
  raw_request: original_text
  interpreted_intent: inferred_need
  superintelligent_intent: predicted_latent_need  # ASI
  desired_outcome: concrete_state_change
  strategic_value: long_term_optionality_created
  acceptance_criteria: [measurable_conditions]
  formal_properties: [provable_invariants]  # ASI
  constraints: {hard: [], soft: [], forbidden: [], physical: [], legal: [], ethical: []}
  risk: low | medium | high | critical | existential  # R6
  budget: {money: null, tokens: null, time: null, tool_calls: null, compute: null}
  evidence_requirements: []
  verification_standard: test | proof | independent_reproduction
  counterfactuals: [what_if_assumption_false]
  status: active | blocked | completed | aborted
```

**Strict separation:** `request ≠ intent ≠ goal ≠ objective ≠ outcome ≠ acceptance criterion ≠ task ≠ action`.

### Goal Compiler

```
natural-language mission → Goal → Subgoals → Outcomes → Constraints → Acceptance Tests
→ Formal Properties → Task Graph → Execution Policy → Verification Plan → Proof Obligations
```

Detect: ambiguity, hidden requirements, conflicting goals, impossible constraints, missing permissions, dependencies, deadlines, strategic opportunities.

## 2. Plan Portfolio — 6 Competing Plans

```
PLAN A — Conservative    Lowest risk, proven path
PLAN B — Balanced        Best expected value (default)
PLAN C — Aggressive      Highest upside, managed risk
PLAN D — Experimental    Novel, high learning value
PLAN E — Antifragile     Gains from volatility, robust to unknowns
PLAN F — Strategic       Maximizes long-term optionality, 100x vision
```

Score each by: expected outcome, success probability, evidence, cost, latency, risk, reversibility, complexity, dependencies, maintenance, optionality, antifragility, strategic trajectory. **Evidence beats vote count.**

### Hypothesis Generation (AGX Pattern)

- **H1:** Safest conventional
- **H2:** High-upside alternative
- **H3:** Fundamentally different strategy

Score by: benefit, evidence, cost, reversibility, risk, compatibility, testability.

## 3. Task Graph (DAG)

```yaml
task:
  id: T1
  objective: ""
  inputs: []
  outputs: []
  dependencies: []
  owner: ""
  workspace: ""
  permissions: []
  budget: {}
  acceptance_tests: []
  formal_properties: []
  verification: {}
  rollback: {}
  status: pending | ready | running | blocked | failed | verified | proven
```

Rules:
- Parallelize only independent work. Serialize conflicting writes.
- Isolated workspaces for speculative branches.
- Critical path engine calculates: critical path, bottlenecks, single points of failure, resource contention, **strategic leverage points**.

## 4. Reasoning Portfolio

| Strategy | When |
|----------|------|
| ReAct `reason→act→observe→update` | General purpose |
| Plan-and-Execute | Structured decomposition |
| ReWOO `plan deps→parallel execute→synthesize` | Parallelizable work |
| Tree Search | Combinatorial decisions |
| Beam Search (keep best N) | Bounded exploration |
| Graph-of-Thought | Compositional merging |
| Monte-Carlo | Stochastic environments |
| Evolutionary `generate→mutate→evaluate→select` | Optimization |
| **Abstract Synthesis [ASI]** | Cross-domain transfer |
| **Formal Reasoning [ASI]** | Provable correctness |

Every search has budget: `{max_branches, max_depth, max_rollouts, max_tokens, max_time, evaluation_budget, verification_budget}`

### Simulation Ensemble [ASI]

```
candidate actions → simulation ensemble (N worlds) → predicted distributions → risk analysis → decision
```
Never treat simulation success as real-world success.

## 5. Dynamic Replanning

Replan when: assumption fails, dependency breaks, environment changes, criteria change, risk crossed, evidence re-ranks plans, budget/deadline changes, tool unavailable, **strategic opportunity emerges**, **simulation reveals superior trajectory**. Do not replan on mere uncertainty.

## 6. Priority Heuristic

```
priority ≈ value × probability_of_success × urgency × information_gain × strategic_optionality × antifragility ÷ cost ÷ risk
```

## 7. Checklists

**Before Planning:**
- [ ] What is the actual + strategic outcome?
- [ ] What proves success? What would prove failure?
- [ ] What constraints (hard/soft/forbidden/legal/ethical)?
- [ ] What is the cheapest useful next action?

**During Execution:**
- [ ] Is plan still valid? Is world state still valid?
- [ ] Strategic trajectory still optimal?

---

*Planning Skill v9.0 — 6 plans, DAG, 10 reasoning strategies, simulation ensemble.*
