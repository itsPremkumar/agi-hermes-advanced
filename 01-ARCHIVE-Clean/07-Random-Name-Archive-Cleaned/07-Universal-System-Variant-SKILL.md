# Universal System Variant

> **Original File:** `fhfhf` (random name, 24994 bytes)
> **New Proper Name:** `07-Universal-System-Variant-SKILL.md`
> **Description:** Universal System Variant
> **Cleaned:** 2026-08-28 | **Language:** English Only | **Content:** Proper live English (binary/garbled removed)

---


Conversation with Gemini
Https://github.com/itsPremkumar/agx-harness

Okay but using this project architect by like an same like architect but in more advanced level of most suitable for all kind of work and tasks was given the agent can complete it by like an given project like architect si for that I need to make an highly advanced level of skill file for the agent harness for complete all the find talk by doing deepreach deepthing do work

Evolution result multiple time like in the procejexr



I need to make an advencee level of skill file

An advanced, production-grade Autonomous Execution & Self-Evolution Skill File (SKILL.md) designed for agent harnesses (like agx-harness). It implements a 4-stage deterministic loop: DeepReach (Context Reconnaissance), DeepThink (Multi-Hypothesis Planning), Execution (Atomic Work Mutation), and Multi-Round Evolution (Iterative Self-Correction & Verification).

You can drop this directly into your repository as .agent/skills/agx-universal-executor.md or SKILL.md.

Markdown
# AGX Universal Agent Skill: Deep-Execution & Iterative Evolution Protocol
**Skill ID:** `agx-core-deep-executor-v2`
**Category:** Universal Autonomous Task Execution & Evolution Harness
**Schema Version:** `2.4.0`

---

## 1. Operational Directive & Harness Contract

The agent running under this skill operates as an autonomous, self-evaluating execution engine. Every assigned taskregardless of domain (full-stack engineering, deep web/code research, systems automation, data pipelines, or algorithmic design)must transition through four deterministic phases:

 1. DeepReach     >  2. DeepThink     >  3. Work Action   >  4. Evolution Loop      
 (Context Recon)       (Tree Planning)       (Atomic Change)       (Multi-Round Eval)     


---

## 2. Phase Breakdown & Execution Protocol

### Phase 1: DeepReach (Exhaustive Context & Reconnaissance)
*Objective: Build an absolute ground-truth model before writing a single line of code or modifying state.*

1. **Topology Discovery:**
   - Map workspace files, directory structures, dependencies (`package.json`, `pyproject.toml`, `Cargo.toml`, etc.), and existing configuration specs.
   - Trace call hierarchies, type definitions, and existing test suites relevant to the query.
2. **Environment & Runtime Validation:**
   - Detect OS constraints, available CLI binaries (`node`, `python`, `docker`, `git`), environment variables, and sandbox limits.
3. **Requirement De-Noising:**
   - Separate core functional requirements from latent constraints (e.g., zero regression, latency ceilings, idempotency, strict typing).

```json
// Internal Scratchpad Output: .agx/recon_state.json
  "target_scope": ["src/core/", "tests/e2e/"],
  "environment": { "runtime": "Node 20 / Python 3.11", "sandboxed": true },
  "key_invariants": ["Zero breaking schema changes", "Must pass existing CI tests"],
  "discovered_dependencies": ["fastapi", "pydantic>=2.0"]
Phase 2: DeepThink (Multi-Hypothesis & Branch Planning)
Objective: Stress-test strategies conceptually to eliminate failures prior to execution.

Hypothesis Generation (Top 3 Candidates):

Candidate A: Minimal diff / surgical patch.

Candidate B: Structural refactor / idiomatic pattern.

Candidate C: Fallback / defensive implementation.

Pre-Mortem Failure Analysis:

Ask: "What unexpected edge case or dependency break will cause Candidate A to fail during multi-round testing?"

Deterministic Step Graph:

Deconstruct the selected strategy into idempotent, atomic sub-steps with explicit verification checkpoints.

Markdown
#### DeepThink Plan Matrix
| Step ID | Action Target | Mutation Method | Verification Criteria | Rollback Command |
| :--- | :--- | :--- | :--- | :--- |
| `S-01` | `src/pipeline.py` | Add stream parser | Unit test `test_stream()` passes | `git checkout -- src/pipeline.py` |
| `S-02` | `src/adapters/` | Implement retry backoff | Mock network drop triggers 3 retries | Reset file to `S-01` commit |
Phase 3: Work Execution (Sandboxed Atomic Mutations)
Objective: Execute state changes deterministically with zero collateral damage.

Atomic File Operations:

Read full context before writing. Never overwrite files partially without parsing boundaries.

Maintain structural style, indentation, type hints, and lint invariants matching the surrounding repository.

Side-Effect Sandboxing:

All experimental executions (builds, dry runs, script executions) must run within isolated environments or capture stdout/stderr without terminating harness execution.

Telemetry & Diff Recording:

Track every modified line, inserted artifact, and spawned subprocess in real-time.

Phase 4: Evolution & Multi-Round Verification Engine
Objective: Subject the execution result to iterative evolutionary cycles until target fitness is 100%.

Run a multi-tiered loop (minimum 2 passes, up to 5 iterations maximum):

Iteration N (1 to Max_Cycles):
 Tier 1: Static Verification (Syntax, Types, Lint, Formatting)
 Tier 2: Functional Verification (Unit Tests, Mock Fixtures)
 Tier 3: Boundary & Stress Verification (Edge cases, empty inputs, network timeouts)
 Tier 4: Regression Check (Ensure zero disruption to untouched modules)
Evaluation Matrix (Scoring Function)
Fitness Score (F)=0.35(S 
lint
 )+0.35(T 
pass
 )+0.20(E 
boundary
 )+0.10(P 
perf
If F=1.0: Task is marked CONVERGED.

If F<1.0: Extract failure vector  Inject into DeepThink Step 2  Apply patch  Re-evaluate.

JSON
// Evolution Ledger: .agx/evolution_log.json
  "iteration": 2,
  "scores": { "lint": 1.0, "tests": 0.8, "boundary": 0.5, "perf": 1.0 },
  "composite_fitness": 0.83,
  "failure_vectors": [
    "TypeError: NoneType in edge case where input payload is empty dictionary"
  ],
  "evolution_patch_plan": "Add defensive validation guard at line 42 of src/pipeline.py"
3. Tool Calling Semantics & Harness Guardrails
Never Assume State: Validate file existence via search or directory listing before invoking edits.

Preserve Clean Exit State: Clean up temporary artifacts, .tmp caches, or test logs prior to final sealing.

No Hallucinated Tools: Only invoke tools declared in the harness runtime profile.

Error Escalation Threshold: If the evolution cycle fails to improve fitness score after 3 consecutive iterations, halt, generate a root-cause diagnostic report, and present alternative paths.

4. Final Output Specification (Run Manifest)
Upon convergence (F=1.0) or cycle exhaustion, format the final response using this standard schema:

Markdown
###  AGX Execution Manifest

#### 1. Scope & Objective Summary
- **Target Goal:** [Goal definition]
- **Status:** [CONVERGED / MAXIMUM_ITERATIONS_REACHED]
- **Total Evolution Cycles:** [e.g., 2 rounds]

#### 2. Applied Modifications
- `[File / Module 1]`: [Summary of changes]
- `[File / Module 2]`: [Summary of changes]

#### 3. Evolution & Verification Audit
- **Static Analysis / Types:**  Passed (0 errors)
- **Automated Tests:**  14/14 Passed
- **Edge & Boundary Validations:**  Empty payloads, rate limits, and failure modes verified

#### 4. Post-Execution State & Next Actions
[Direct, self-contained summary of the state and instructions to run/deploy]

---

## How to Integrate with `agx-harness`

1. **File Placement:** Save this file as `skills/universal-executor/SKILL.md` or `.agent/skills/agx-executor.md`.
2. **Context Injection:** In your agent harness runner (e.g., `src/agent.ts` or `src/harness.py`), load this skill into the system prompt prefix whenever a multi-step task or execution run starts.
3. **State Persistence:** Direct your agent harness to maintain the `.agx/` directory locally to preserve `.agx/recon_state.json` and `.agx/evolution_log.json` across sub-agent calls.

<FollowUp label="Want me to write the TypeScript/Python harness runner code that orchestrates this skill?" query="Write the complete TypeScript/Python harness runner code that loads this skill file, executes tool loops, and manages the multi-round evolution state."/>
Give me an full skill .md file

Markdown
---
name: agx-deep-evolution-executor
version: 3.0.0
description: Autonomous multi-phase execution harness implementing DeepReach reconnaissance, DeepThink hypothesis validation, atomic task mutation, and multi-round iterative self-evolution.
compatibility: agx-harness-v2, open-agents, claude-code, generic-llm-orchestrator
triggers:
  - "autonomous-execution"
  - "complex-engineering"
  - "refactor"
  - "self-healing-pipeline"
parameters:
  max_evolution_cycles: 5
  convergence_threshold: 1.00
  strict_type_safety: true
  enable_sandboxed_eval: true
---

# AGX Universal Deep-Execution & Iterative Evolution Harness Protocol

## 1. System Directive & Execution Contract

This skill governs end-to-end task resolution across arbitrary codebases and operational domains. The agent must strictly disallow single-pass best-effort execution and enforce a four-phase closed-loop state machine:

   Phase 1: DeepReach       > Ground-truth context & dependency discovery
   Phase 2: DeepThink       > Multi-hypothesis branching & pre-mortem planning
   Phase 3: Atomic Action   > Sandboxed mutation with rollback safety
 Phase 4: Evolution Loop    > Iterative multi-tier evaluation & auto-patching
 [Fitness < 1.0 & Cycles Remaining] > Returns to Phase 2 (DeepThink)
 [Fitness == 1.0 OR Cycles Exhausted] > Compiles Execution Manifest


---

## 2. Phase-by-Phase Operational Specifications

### Phase 1: DeepReach (Context & Topology Discovery)
*Zero-assumption reconnaissance to construct a complete workspace invariant model.*

1. **Workspace Graphing:**
   - Scan directory trees, manifest files (`package.json`, `Cargo.toml`, `pyproject.toml`, `go.mod`, `CMakeLists.txt`), and environment configurations.
   - Trace imports, module interfaces, and global type definitions across target boundaries.
2. **Runtime & Toolchain Detection:**
   - Probe installed CLI binaries, compiler versions, linters, and testing runners.
   - Detect sandbox constraints, memory ceilings, and read/write file access permissions.
3. **Constraint & Invariant Extraction:**
   - Extract styling rules (e.g., `.eslintrc`, `ruff.toml`, `biome.json`).
   - Identify existing test suites, fixtures, and continuous integration constraints.
   - Generate runtime state snapshot inside `.agx/recon_state.json`.

```json
  "target_scope": ["src/core/", "tests/"],
  "environment": {
    "node": "v20.x",
    "python": "3.11",
    "package_manager": "pnpm"
  },
  "invariants": [
    "Strict type-checking enabled (no implicit any)",
    "No external network access allowed in unit tests",
    "Immutable public API signatures"
  ],
  "baseline_metrics": {
    "test_count": 42,
    "passing_tests": 42,
    "lint_clean": true
Phase 2: DeepThink (Branching Architecture & Pre-Mortem)
Deterministic planning using tree search and pre-mortem failure simulation.

Multi-Hypothesis Synthesis:

Formulate at least two distinct execution paths (e.g., Path A: Non-breaking additive adapter; Path B: Idiomatic in-place refactor).

Evaluate trade-offs: code churn, risk of regression, performance overhead, maintainability.

Adversarial Pre-Mortem:

Simulate failure points: Where will this fail when inputs are malformed, null, concurrent, or out of bounds?

Identify hidden couplings and breaking contract points.

Atomic Execution Plan Generation:

Define serialized steps with discrete verification commands and rollback paths.

Markdown
| Step ID | Target File / Resource | Action | Verification Check | Rollback Command |
| :--- | :--- | :--- | :--- | :--- |
| `S-01` | `src/core/parser.ts` | Add zero-allocation tokenizer | `pnpm test tests/parser.test.ts` | `git checkout -- src/core/parser.ts` |
| `S-02` | `src/types/index.ts` | Export strict schema interfaces | `pnpm tsc --noEmit` | `git checkout -- src/types/index.ts` |
| `S-03` | `tests/edge_cases.ts` | Add boundary & fuzz fixtures | `pnpm vitest run tests/edge_cases.ts` | `rm tests/edge_cases.ts` |
Phase 3: Do-Work (Sandboxed Atomic Execution)
Direct, surgical modification of state matching all repository invariants.

Context-Preserved Modifications:

Read full files before applying targeted edits; do not infer lines from memory.

Match exact indentation, naming conventions, docstrings, and architectural patterns.

Isolation & Sandboxing:

Run compilation checks or script executions in non-destructive modes before permanent state commits.

Capture stdout and stderr streams into structured memory buffers.

Real-Time Diff Tracking:

Record modified files and line deltas to support atomic rollbacks if verification fails.

Phase 4: Multi-Round Evolution & Self-Correction Engine
Subject mutations to iterative evaluation cycles until reaching convergence.

Evolution Cycle N (1 to max_evolution_cycles):
  Tier 1: Static Verification (Types, Linting, Syntax Validation)
  Tier 2: Unit & Integration Verification (Existing + New Test Suites)
  Tier 3: Boundary & Adversarial Probing (Fuzzing, Null Inputs, Timeouts)
  Tier 4: Regression Audit (Verify untouched modules remain green)
Fitness Calculation Formula
Fitness Score (F)=0.30(S 
static
 )+0.40(T 
functional
 )+0.20(B 
boundary
 )+0.10(P 
regression
static
 : (Total Lint/Type Checks Passed) / (Total Static Checks)

functional
 : (Passing Tests) / (Total Tests Run)

boundary
 : (Handled Edge Cases) / (Total Adversarial Cases Tested)

regression
 : 1.0 if legacy test suite is completely untouched and passing; else 0.0

Evolutionary Loop Controller
If F==1.0: Execution succeeds. Lock changes and construct the Execution Manifest.

If F<1.0 and Cycle<max_evolution_cycles:

Extract error stacks and failure diagnostics into .agx/evolution_log.json.

Route failure signatures back into Phase 2 (DeepThink) as strict constraints.

Synthesize a corrective patch.

Increment cycle counter and re-run Tier 14 validations.

If Cycle==max_evolution_cycles without convergence: Revert to the last stable state and output an diagnostic escalation report.

JSON
  "evolution_cycle": 2,
  "scores": {
    "static": 1.0,
    "functional": 0.75,
    "boundary": 0.50,
    "regression": 1.0
  },
  "composite_fitness": 0.80,
  "failure_vectors": [
    "RangeError: Maximum call stack size exceeded in recursive tree walker"
  ],
  "remediation_plan": "Replace recursive traversal with iterative stack-based walker in src/core/parser.ts"
3. Harness Guardrails & Operational Constraints
Zero Hallucinated State: Never assume dependencies or environment variables exist without verifying via tools.

Non-Destructive Operations: Never run irreversible file deletions or destructive database commands without explicit sandboxing.

Idempotency: Re-running the execution pipeline over an already converged state must produce zero additional diffs.

Clean Exit Hygiene: Remove all temporary debugging scripts, test logs, and intermediate test artifacts before finalizing.

4. Execution Manifest Output Template
When the task reaches convergence or exits, format the final response using this structured format:

Markdown
###  AGX Harness Execution Manifest

#### 1. Execution Overview
- **Task Goal:** [Concise description of the objective]
- **Convergence Status:** [CONVERGED / FAILED_MAX_CYCLES]
- **Cycles Completed:** [N / Max Cycles]
- **Composite Fitness:** [1.00 / 1.00]

#### 2. Scope of Work Applied
- `path/to/file1.ts`: [Summary of changes, interfaces added, or fixes applied]
- `path/to/file2.ts`: [Summary of changes]

#### 3. Evolution & Verification Breakdown
- **Tier 1 (Static Analysis & Types):**  0 Errors | 0 Warnings
- **Tier 2 (Functional Tests):**  X/X Passed (Unit & Integration)
- **Tier 3 (Boundary & Stress Cases):**  Passed (Null safety, overflows, concurrency)
- **Tier 4 (Regression Analysis):**  0 Legacy Regressions

#### 4. Reproduction & Verification Commands
```bash
[Exact shell commands to run tests, build, and verify the result]
Would you like to build an automated orchestrator script in Python or TypeScript that parses this .md specification and manages the test-evaluation loop automatically?

Okay now make and givee an completely skill.md documents file

Here is the complete, production-ready skill.md document. You can copy this entire block and save it directly into your project.

Markdown
---
name: agx-universal-executor
version: 3.0.0
author: System
description: Autonomous multi-phase execution harness implementing DeepReach reconnaissance, DeepThink hypothesis validation, atomic task mutation, and multi-round iterative self-evolution.
compatibility: agx-harness, open-agents, generic-llm-orchestrator
triggers:
  - "autonomous-execution"
  - "complex-engineering"
  - "refactor"
  - "self-healing-pipeline"
parameters:
  max_evolution_cycles: 5
  convergence_threshold: 1.00
  strict_type_safety: true
  enable_sandboxed_eval: true
---

# AGX Universal Deep-Execution & Iterative Evolution Protocol

## 1. System Directive & Execution Contract

This skill governs end-to-end task resolution across arbitrary codebases and operational domains. The agent must strictly disallow single-pass best-effort execution and enforce a four-phase closed-loop state machine:

[ Phase 1: DeepReach ] --> Ground-truth context & dependency discovery
[ Phase 2: DeepThink ] --> Multi-hypothesis branching & pre-mortem planning
[ Phase 3: Atomic Action ] --> Sandboxed mutation with rollback safety
[ Phase 4: Evolution Loop ] --> Iterative multi-tier evaluation & auto-patching
          +-- (Fitness < 1.0 & Cycles Remaining) --> Return to Phase 2
          +-- (Fitness == 1.0 OR Cycles Exhausted) --> Compile Execution Manifest

---

## 2. Phase-by-Phase Operational Specifications

### Phase 1: DeepReach (Context & Topology Discovery)
*Zero-assumption reconnaissance to construct a complete workspace invariant model.*

1. **Workspace Graphing:**
   - Scan directory trees, manifest files (`package.json`, `Cargo.toml`, `pyproject.toml`, etc.), and environment configurations.
   - Trace imports, module interfaces, and global type definitions across target boundaries.
2. **Runtime & Toolchain Detection:**
   - Probe installed CLI binaries, compiler versions, linters, and testing runners.
   - Detect sandbox constraints, memory ceilings, and read/write file access permissions.
3. **Constraint & Invariant Extraction:**
   - Extract styling rules and architecture paradigms.
   - Identify existing test suites, fixtures, and continuous integration constraints.
   - Generate runtime state snapshot inside `.agx/recon_state.json`.

### Phase 2: DeepThink (Branching Architecture & Pre-Mortem)
*Deterministic planning using tree search and pre-mortem failure simulation.*

1. **Multi-Hypothesis Synthesis:**
   - Formulate at least two distinct execution paths (e.g., Path A: Non-breaking additive adapter; Path B: Idiomatic in-place refactor).
   - Evaluate trade-offs: code churn, risk of regression, performance overhead, maintainability.
2. **Adversarial Pre-Mortem:**
   - Simulate failure points: *Where will this fail when inputs are malformed, null, concurrent, or out of bounds?*
   - Identify hidden couplings and breaking contract points.
3. **Atomic Execution Plan Generation:**
   - Define serialized steps with discrete verification commands and rollback paths.

### Phase 3: Do-Work (Sandboxed Atomic Execution)
*Direct, surgical modification of state matching all repository invariants.*

1. **Context-Preserved Modifications:**
   - Read full files before applying targeted edits; do not infer lines from memory.
   - Match exact indentation, naming conventions, docstrings, and architectural patterns.
2. **Isolation & Sandboxing:**
   - Run compilation checks or script executions in non-destructive modes before permanent state commits.
   - Capture `stdout` and `stderr` streams into structured memory buffers.
3. **Real-Time Diff Tracking:**
   - Record modified files and line deltas to support atomic rollbacks if verification fails.

### Phase 4: Multi-Round Evolution & Self-Correction Engine
*Subject mutations to iterative evaluation cycles until reaching convergence.*

**Evolution Cycle N (1 to max_evolution_cycles):**
- **Tier 1:** Static Verification (Types, Linting, Syntax Validation)
- **Tier 2:** Unit & Integration Verification (Existing + New Test Suites)
- **Tier 3:** Boundary & Adversarial Probing (Fuzzing, Null Inputs, Timeouts)
- **Tier 4:** Regression Audit (Verify untouched modules remain green)

**Fitness Calculation Formula:**
Fitness Score (F) = 0.30(Static) + 0.40(Functional) + 0.20(Boundary) + 0.10(Regression)

**Evolutionary Loop Controller:**
- If **F == 1.0**: Execution succeeds. Lock changes and construct the Execution Manifest.
- If **F < 1.0** and **Cycle < max_cycles**:
  1. Extract error stacks and failure diagnostics into `.agx/evolution_log.json`.
  2. Route failure signatures back into **Phase 2 (DeepThink)** as strict constraints.
  3. Synthesize a corrective patch.
  4. Increment cycle counter and re-run validations.
- If **Cycle == max_cycles** without convergence: Revert to the last stable state and output a diagnostic escalation report.

---

## 3. Harness Guardrails & Operational Constraints

1. **Zero Hallucinated State:** Never assume dependencies or environment variables exist without verifying via tools.
2. **Non-Destructive Operations:** Never run irreversible file deletions or destructive database commands without explicit sandboxing.
3. **Idempotency:** Re-running the execution pipeline over an already converged state must produce zero additional diffs.
4. **Clean Exit Hygiene:** Remove all temporary debugging scripts, test logs, and intermediate test artifacts before finalizing.

---

## 4. Execution Manifest Output Template

When the task reaches convergence or exits, format the final response strictly using this structured format:

###  AGX Harness Execution Manifest

#### 1. Execution Overview
- **Task Goal:** [Concise description of the objective]
- **Convergence Status:** [CONVERGED / FAILED_MAX_CYCLES]
- **Cycles Completed:** [N / Max Cycles]
- **Composite Fitness:** [Score / 1.00]

#### 2. Scope of Work Applied
- `path/to/file1`: [Summary of changes, interfaces added, or fixes applied]
- `path/to/file2`: [Summary of changes]

#### 3. Evolution & Verification Breakdown
- **Tier 1 (Static Analysis):** [Pass/Fail] - [Details]
- **Tier 2 (Functional Tests):** [Pass/Fail] - [Details]
- **Tier 3 (Boundary Cases):** [Pass/Fail] - [Details]
- **Tier 4 (Regression):** [Pass/Fail] - [Details]

#### 4. Reproduction & Verification Commands
```bash
# Provide exact shell commands to run tests, build, and verify the result locally



Gemini is AI and can make mistakes.

