---
name: agi-memory-world
version: "9.0"
parent: agi-master-router
scope: World Model, Epistemics, Evidence, Context, Memory, Temporal Reasoning
planes: [World Model, Memory, Context, Cognition]
---

# SKILL 06 — MEMORY, WORLD MODEL & CONTEXT

> **Load this skill when:** Task needs world state tracking, memory recall/storage, context management, or epistemic rigor.
> **Load FIRST in any full mission** — establishes the world model before research and planning.

---

## 1. World Model — Multi-Horizon Superintelligent

```yaml
world:
  entities: []
  relationships: []
  resources: []
  capabilities: []
  environment: {}
  tasks: []
  dependencies: []
  observations: []
  events: []
  assumptions: []
  hypotheses: []
  risks: []
  commitments: []
  external_state: {}
  temporal_state: {past: {}, present: {}, future_scenarios: []}  # ASI
  causal_models: []                     # cause → mechanism → effect
  counterfactual_worlds: []             # ASI what-if simulations
  simulation_ensemble: []               # ASI multiple futures
  unknowns: []
  known_unknowns: []
  unknown_unknowns_estimate: 0.0        # ASI humility metric
```

Every transition:

```yaml
transition: {before: {}, action: {}, observation: {}, after: {}, timestamp: "", actor: "", source: "", confidence: confirmed|supported|likely|plausible|uncertain, evidence: [], causal_hypothesis: "", reversible: true|false|unknown, strategic_implication: ""}
```

**Multi-Horizon Temporal Modeling [ASI]:**
- Past: causal reconstruction of what happened and why
- Present: what is true now with confidence intervals
- Near future: next 24h with scenarios
- Strategic future: next 90 days with branching trajectories

Distinguish: `completed | currently_true | in_progress | scheduled | expected | conditional | speculative | strategically_projected [ASI]`

## 2. Epistemic Superintelligence

```yaml
claim:
  id: ""
  text: ""
  status: fact | observed | sourced | inferred | hypothesis | prediction | assumption | unknown | contradicted | obsolete
  bayesian_prior: 0.0
  bayesian_posterior: 0.0
  sources: []
  confidence: 0.0-1.0
  calibration_score: 0.0
  verification_method: ""
  falsification_test: "what would prove this wrong"
  last_verified: ""
  expires_at: ""
  conflicting_claims: []
  cross_domain_support: []
```

| Status | Meaning | ASI Precision |
|--------|---------|---------------|
| fact | Directly supported | Bayesian posterior >0.95 + independent corroboration |
| observed | Actually measured | Sensor trace with provenance |
| hypothesis | Testable | Includes falsification criterion |
| unknown | Not established | Classified as known-unknown vs unknown-unknown |
| contradicted | Evidence conflicts | Both sides preserved with adjudication plan |

**Never allow `assumption → fact` without evidence.** Even superhuman repetition doesn't make it true.

### Evidence Graph

```
Claim → Source → Evidence → Counter-evidence → Method → Timestamp + Decay → Reliability → Dependency → Bayesian Weight → Cross-domain Corroboration
```

For consequential claims: `claim → primary source → independent source → contradiction search → freshness check → adversarial challenge → formal verification → confidence update`

### Source Reliability

```
reliability = authority + primary_status + recency + transparency + corroboration + specificity + independence + reproducibility - conflict - unverifiable - stale - circular_citation
```

### Contradiction Engine

```
belief → support search → contradiction search → ≥3 alternatives → adversarial challenge → independent verification → Bayesian update → posterior
```

## 3. Context Operating System — Hierarchical

Context is a FINITE managed resource:

```
WRITE → SELECT → RANK → COMPRESS → ISOLATE → ARCHIVE → RESTORE → SYNTHESIZE [ASI]
```

Optimize for: relevance, decision impact, freshness, uncertainty, dependency, source quality, token cost, strategic value, cross-domain relevance.

**Hierarchical Compression [ASI]:**
- L1: Raw observations (full fidelity, short TTL)
- L2: Extracted facts (deduplicated, provenance-tagged)
- L3: Synthesized insights (compressed, high importance)
- L4: Strategic abstractions (cross-mission, permanent)

Before consequential reasoning, create:

```yaml
context_packet: {mission: {}, current_goal: {}, acceptance_tests: [], constraints: [], permissions: [], relevant_world_state: {}, relevant_memory: [], evidence: [], contradictory_evidence: [], hypotheses: [], active_plan: {}, failures: [], pending_commitments: [], available_tools: [], known_limitations: [], strategic_context: {}, cross_domain_analogies: []}
```

## 4. Memory OS — 15 Namespaces

```
working, episodic, semantic, procedural, organizational, failure, evaluation,
world-state, skill, research, decision, causal, preference, identity,
strategic [ASI], superintelligent_insight [ASI]
```

**Lifecycle:**
```
observe → score → normalize → deduplicate → validate → resolve conflicts
→ synthesize → assign provenance → TTL → hierarchical compress → store
→ retrieve → evaluate retrieval → consolidate → cross-domain index [ASI]
```

**Importance:**
```
importance = future_reuse × consequence × reconstruction_cost × identity_relevance × verification_strength × cross_domain_transferability [ASI] × strategic_value [ASI]
```

Conflict resolution evaluates: source authority, freshness, direct observation, corroboration, context, confidence, scope, expiration. Record `{memory_a, memory_b, resolution, evidence, confidence, strategic_implication}`. Never silently overwrite.

### Sleep-Time Superintelligence [ASI]

When idle, bounded background work: memory consolidation, hierarchical compression, research continuation, benchmarking, failure analysis, skill extraction, tool testing, index maintenance, plan preparation, multi-future simulation, candidate generation, evaluation, knowledge graph maintenance, **autonomous hypothesis generation**, **cross-mission pattern mining**, **self-model improvement**. All bounded, interruptible, observable, budgeted, permission-aware, reversible.

## 5. Hypothesis Ledger

```yaml
hypothesis:
  id: H-123
  claim: ""
  confidence: 0.0
  supporting_evidence: []
  opposing_evidence: []
  predictions: []
  tests: []
  status: active | supported | rejected | unknown
```

## 6. Cognition Enhancements (Memory-Linked)

**Confidence Calibration:**
```yaml
confidence: {value: 0.0-1.0, basis: "", evidence_count: 0, independent_sources: 0, contradictory_sources: 0, uncertainty: "", calibration_history: [], bayesian_posterior: 0.0}
```
Track `predicted confidence vs actual success` → Brier score → calibration curve.

**Causal:** `hypothesis → intervention → observation → causal update` with confounder modeling.

**Counterfactual:** For high-impact choices evaluate `A happens / B happens / nothing / assumption X false / resource Y disappears / environment changes / adversary responds / black swan`. Ask: *What evidence would make the current plan catastrophically wrong?*

---

*Memory & World Skill v9.0 — Multi-horizon world model, Bayesian epistemics, 15 namespaces, hierarchical context.*
