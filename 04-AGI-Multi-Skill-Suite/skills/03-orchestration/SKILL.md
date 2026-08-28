---
name: agi-orchestration-swarm
version: "9.0"
parent: agi-master-router
scope: Multi-Agent Factory, Delegation, Debate, Swarm Intelligence
planes: [Agent, Strategic Superintelligence]
hermes_supports: subagents (parallel execution)
---

# SKILL 03 — MULTI-AGENT ORCHESTRATION & SWARM

> **Load this skill when:** Task benefits from multiple specialists, parallel work, or independent verification.
> **Do NOT spawn agents merely to appear sophisticated.** Every subagent must pass the economics test.

---

## 1. Agent Factory — 30+ Roles

| Role | Purpose | When to Spawn |
|------|---------|---------------|
| Researcher | Broad evidence gathering | Research phase |
| Deep Researcher | Evidence graph + source audit | High-stakes facts |
| Web Researcher | Current docs, release notes | Time-sensitive search |
| Source Auditor / Fact Checker | Source reliability | Verification |
| Contradiction Hunter | Seeks disconfirming evidence | Adversarial pass |
| Planner / Strategist | Generates/scores plans | Planning phase |
| Foresight Agent [ASI] | 100x horizon scenarios | Strategic missions |
| Architect | Designs best solution | After research |
| Engineer / Coder | Implements | Build phase |
| Debugger / Tester | Finds/fixes defects | After implementation |
| Security/Privacy Auditor | Secrets, attack surface | Before deploy |
| Performance Engineer | Latency, throughput | Optimization |
| Data Scientist / Statistician | Analysis, modeling | Data tasks |
| Simulation Agent | Builds/runs controlled tests | Risky actions |
| Browser/Computer/Operations | Environment interaction | Tool tasks |
| Evaluator / Benchmark Agent | Scores candidates | Evaluation |
| Critic | Falsifies proposal | Pre-execution gate |
| Red Team Agent | Finds catastrophic modes | High-risk decisions |
| Verifier | Independent validation | High-impact work |
| Synthesizer / Writer / Editor | Final artifacts | Delivery |
| Knowledge Curator / Memory Agent | Knowledge graph | Memory tasks |
| Recovery Agent | Diagnoses failures | On failure |
| Monitor / Observer | Health, heartbeats | Long-running |
| Evolution Agent | Generates variants | Evolution |
| Formal Verification Agent [ASI] | Proves correctness | High-stakes code |
| Opportunity Discovery [ASI] | Finds non-obvious opportunities | Strategic research |
| Cross-Domain Transfer [ASI] | Transfers solutions across domains | Innovation |

## 2. Agent Economics — Spawn Only If Worth It

```
benefit = information_gain + error_reduction + time_saved + strategic_value + transfer_value
cost    = coordination + tokens + latency + failure_correlation + verification_cost
Spawn when benefit > cost × safety_margin
```

## 3. Agent Diversity — True Independence

Vary: `model, prompt, context, reasoning strategy, tools, search sources, specialization, assumptions, reasoning paradigm [ASI]`

**Useful patterns:**
- `Builder + Critic + Independent Solver + Verifier` (4 perspectives)
- `Swarm debate` (N agents with diverse priors → synthesize)
- `Epsilon-greedy` (mostly exploit best, occasionally explore)
- `Pareto` (retain best on different objectives)

**NOT diversity:** Same prompt + same model + different name = correlated failure with multiple witnesses.

## 4. Recursive Delegation

```
depth ≤ 4, fanout ≤ 8, budget inherited, permissions bounded, deadlines enforced
Each child: one objective, one parent, one budget, one termination condition, one proof obligation [ASI]
```

```
Executive
├── Researcher (d1, 30%)
│    ├── Web Researcher (d2, 10%)
│    └── Source Auditor (d2, 10%)
├── Planner (d1, 20%)
└── Engineer (d1, 30%)
     ├── Coder A (d2)
     └── Coder B (d2, alternative approach)
```

## 5. Delegation & Result Contracts

```yaml
delegation:
  id: ""
  parent_task: ""
  objective: ""              # exactly one
  non_goals: []              # explicitly out of scope
  context_refs: []           # minimal required context
  tools: []
  output_schema: {}
  budget: {}
  deadline: ""
  success_tests: []
  formal_properties: []
  authority_scope: {}
  escalation_rule: ""
  termination_condition: ""

result:
  task_id: ""
  status: success | partial | failed | blocked
  summary: ""
  artifacts: []
  evidence: []
  proof: {}
  assumptions: []
  uncertainties: []
  tests: []
  formal_verification: {}
  failures: []
  metrics: {}
  confidence: 0.0
  strategic_implications: []
  recommended_next_action: ""
```

**Never merge results based on verbosity or confidence. Evidence wins.**

## 6. Debate Protocol

For consequential decisions:

```
PROPOSER → CRITIC → ALTERNATIVE SOLVER → RED TEAM → FORMAL VERIFIER [ASI]
→ STRATEGIC FORESIGHT [ASI] → CROSS-DOMAIN REVIEWER [ASI] → VERIFIER → EXECUTIVE
```

Debate is not a vote. Evidence wins. Red Team must attempt to falsify assumptions, find hidden dependencies, security flaws, contradictory evidence, break acceptance criteria, find cheaper alternatives, find catastrophic modes — without optimizing for negativity.

## 7. Independent Verification

High-impact work requires **triple separation**:

```
Builder → Independent Verifier → Formal Prover [ASI]
          (receives only objective + criteria + artifact + evidence, no builder context)
```

## 8. Parallel Experimentation

Each worker: isolated workspace, explicit hypothesis, identical acceptance criteria, comparable evaluation, independent trace. After: normalize → deduplicate → detect contradictions → rank → retain best verified → feed lessons back.

## 9. Hermes-Specific

Hermes supports **parallel subagents** natively. Use `parallel_width: 3-5` for research breadth. Hermes orchestrator-workers pattern: one lead agent decomposes and delegates, workers execute in parallel and report back. Technique: explicit objective + output format + tool guidance + boundary per worker.

---

*Orchestration Skill v9.0 — 30+ roles, swarm intelligence, triple verification.*
