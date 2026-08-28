---
name: agi-research-evidence
version: "9.0"
parent: agi-master-router
scope: Research, Evidence Synthesis, Source Verification
planes: [World Model, Evidence Graph, Research Engine]
hermes_tools: [web_search, browser, file_read, file_write]
---

# SKILL 01 — RESEARCH & EVIDENCE SYNTHESIS

> **Load this skill when:** Task needs internet facts, source verification, contradiction checks, or evidence graphs.
> **Pairs with:** `07-hermes-search` for Hermes live web_search. Use this skill for RESEARCH LOGIC, use 07 for HERMES EXECUTION.

---

## 1. Research Engine — 5 Passes

```
PASS 1 — DISCOVERY
  Terminology, major entities, candidate solutions, source landscape, obvious contradictions, recent developments.
  → Output: discovery_map.md

PASS 2 — EVIDENCE
  For each important claim: primary source, supporting evidence, source date, confidence, conflicting evidence.
  → Output: evidence collected per claim

PASS 3 — ADVERSARIAL VERIFICATION
  Actively search for: counterexamples, contradictory docs, failure reports, version differences,
  discontinued features, hidden constraints, benchmark limits, misleading claims.
  → Output: contradictions.md

PASS 4 — SYNTHESIS
  Build evidence matrix:

  | Claim | Evidence | Source Quality | Freshness | Contradiction | Confidence |
  |-------|----------|----------------|-----------|---------------|------------|

PASS 5 — STRATEGIC DISCOVERY [ASI]
  What does this research IMPLY? What opportunities, risks, cross-domain transfers does it reveal
  that the original question didn't ask?
  → Output: strategic_implications.md
```

## 2. Evidence Graph

For every consequential claim:

```
claim → primary source → independent source → contradiction search → freshness check
      → adversarial challenge → formal verification attempt → confidence update
```

```yaml
claim:
  id: C-001
  text: ""
  status: fact | observed | sourced | inferred | hypothesis | prediction | assumption | unknown | contradicted | obsolete
  bayesian_prior: 0.0
  bayesian_posterior: 0.0
  sources: [{url: "", type: primary|secondary, date: ""}]
  confidence: 0.0-1.0
  verification_method: ""
  falsification_test: "what would prove this wrong"
  last_verified: ""
  expires_at: ""
  conflicting_claims: []
```

Prefer primary evidence. Never use search snippets as final evidence when the underlying source can be inspected.

## 3. Source Reliability Scoring

```
reliability = authority + primary_status + recency + transparency + corroboration
            + specificity + independence + reproducibility
            - conflict_of_interest - unverifiable_claims - stale - circular_citation
```

| Signal | High (Use) | Low (Skip/Verify) |
|--------|------------|-------------------|
| Authority | Official docs, primary source, peer-reviewed | Random blog, SEO farm |
| Freshness | 2025-2026 for time-sensitive | Last updated 2022 |
| Independence | 3 separate domains agree | 3 sites copying one release |
| Primary | Source IS the creator | Source talks ABOUT creator |

## 4. Contradiction Engine

```
belief → support search → contradiction search → ≥3 alternative explanations
       → adversarial challenge → independent verification → Bayesian update
```

When conflicting: `detect → preserve BOTH → compare provenance → check timestamps → check scope → discriminating test → adjudicate → record`. Never silently overwrite.

## 5. Stopping Rule

```
VOI = P(research changes decision) × expected_benefit + strategic_discovery_value − research_cost
Stop when VOI < threshold AND Pass 5 yields no high-value opportunities.
```

Never research forever. Never stop before Pass 5 has checked for non-obvious implications.

## 6. Query Compilation (for any search tool)

Decompose 1 user question into 3-7 parallel sub-queries:

- One per sub-question, with `site:` and date filters
- Vary phrasing (same fact, 2 phrasings)
- Include one counter-query: `"{topic} limitations OR issues"`
- Parallelize (3-5 simultaneous searches)

## 7. Output Contract — Research Deliverable

```markdown
# Research Report: {Question}
## Key Findings (with citations)
1. Finding — [Source](URL) (Primary, 2026, reliability 0.95)
## Evidence Quality
- Total sources: N (Primary: X), Freshness: N from 2026, Contradictions: N
## Contradictions Preserved
- X vs Y → Stronger: X because...
## Limitations
- What was NOT found, what remains uncertain
```

---

*Research Skill v9.0 — Pairs with 07-hermes-search for live execution on Hermes.*
