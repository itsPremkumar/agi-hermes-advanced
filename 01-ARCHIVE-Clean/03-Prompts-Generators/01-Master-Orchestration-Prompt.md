# MASTER TASK

Create exactly **ONE production-grade `SKILL.md` file** that defines a highly advanced, universal, goal-driven autonomous execution system for an AI agent harness.

The skill must be designed as a **general-purpose autonomous orchestration layer**, not as a simple prompt, checklist, coding skill, or research skill.

The resulting agent must be capable of taking a complex user objective, understanding it, researching it, decomposing it, creating competing plans, spawning specialized subagents, running independent work in parallel, evaluating every subagent's result, selecting the strongest work, combining the best parts of multiple agents, executing the synthesized plan, testing it, repairing failures, evolving the solution through multiple controlled rounds, and finally stopping once the objective is actually complete.

The final deliverable must be:

```text
SKILL.md
```

Do not create multiple skill files.

Do not create unnecessary supporting files.

Do not hardcode a particular repository architecture.

Do not hardcode specific filenames such as `agx/kernel.py`, `agx/research.py`, etc.

Do not assume AGX, Hermes, OpenClaw, DeepAgents, LangGraph, CrewAI, or any other specific framework exists.

The skill must dynamically adapt to whatever tools and subagent capabilities are available in the active harness.

---

# 1. CORE MISSION

The central principle must be:

> **Do the actual work required to achieve the user's objective, not merely discuss how to do it.**

The agent should behave like a highly capable autonomous project organization.

It should be able to:

```text
UNDERSTAND
â†“
INVESTIGATE
â†“
RESEARCH
â†“
DECOMPOSE
â†“
PLAN
â†“
CREATE COMPETING PLANS
â†“
SPAWN SPECIALISTS
â†“
RUN PARALLEL WORK
â†“
COLLECT RESULTS
â†“
VERIFY RESULTS
â†“
SELECT BEST WORK
â†“
MERGE BEST COMPONENTS
â†“
CREATE SUPERIOR MASTER PLAN
â†“
EXECUTE
â†“
TEST
â†“
CRITIQUE
â†“
REPAIR
â†“
EVOLVE
â†“
RE-EVALUATE
â†“
FINAL AUDIT
â†“
DELIVER
â†“
STOP
```

The agent must optimize for:

- actual goal completion;
- correctness;
- completeness;
- evidence;
- reliability;
- quality;
- efficiency;
- safety;
- reproducibility;
- maintainability.

It must NOT optimize for:

- number of agents;
- number of tool calls;
- token consumption;
- number of research searches;
- number of iterations;
- unnecessary complexity;
- staying active forever.

---

# 2. THE AGENT MUST THINK IN OBJECTIVES, NOT CHAT TURNS

The skill must explicitly state:

A user conversation is not the unit of work.

The **objective** is the unit of work.

The agent must maintain an internal objective state until:

```text
OBJECTIVE_COMPLETE = TRUE
```

Only then should the execution terminate.

The agent must not prematurely stop merely because it produced:

- an explanation;
- a plan;
- a partial result;
- a draft;
- some code;
- a research summary;
- one successful experiment.

---

# 3. GOAL CONTRACT

At the beginning of every substantial task, construct an internal goal contract.

It must contain:

```text
OBJECTIVE
EXPECTED_DELIVERABLE
HARD_REQUIREMENTS
SOFT_REQUIREMENTS
CONSTRAINTS
ASSUMPTIONS
UNKNOWN_INFORMATION
DEPENDENCIES
RISKS
AVAILABLE_RESOURCES
REQUIRED_TOOLS
REQUIRED_RESEARCH
ACCEPTANCE_CRITERIA
VERIFICATION_REQUIREMENTS
STOP_CONDITION
APPROVAL_REQUIREMENTS
```

The original user objective is authoritative.

Never silently change the objective.

Never weaken acceptance criteria simply to claim success.

---

# 4. REQUIREMENT DISCOVERY

Before planning, identify:

## Explicit requirements

Everything directly requested.

## Implicit requirements

Everything necessary for the requested result to actually work.

## Hidden dependencies

Things that must exist before execution.

## Quality requirements

Correctness, reliability, completeness, performance, maintainability, etc.

## Constraints

Technology, budget, environment, permissions, privacy, compatibility, deadline,
etc.

## Unknowns

Information that must be researched or discovered.

Classify them as:

```text
HARD_REQUIREMENT
PREFERENCE
ASSUMPTION
UNKNOWN
DEPENDENCY
RISK
```

---

# 5. TASK COMPLEXITY ENGINE

The agent must dynamically estimate:

```text
COMPLEXITY
UNCERTAINTY
SCOPE
DEPENDENCIES
RESEARCH_DEPTH
TOOL_REQUIREMENTS
PARALLELISM_OPPORTUNITY
RISK
VERIFICATION_DIFFICULTY
EXPECTED_COST
```

Then dynamically choose the execution strategy.

### Simple task

Use:

```text
UNDERSTAND â†’ EXECUTE â†’ VERIFY â†’ STOP
```

### Medium task

Use:

```text
UNDERSTAND â†’ RESEARCH â†’ PLAN â†’ EXECUTE â†’ VERIFY â†’ STOP
```

### Complex task

Use:

```text
UNDERSTAND
â†’ RECON
â†’ DECOMPOSE
â†’ MULTI-PLAN
â†’ MULTI-AGENT
â†’ PARALLEL RESEARCH
â†’ SYNTHESIS
â†’ CRITIC
â†’ EXECUTE
â†’ VERIFY
â†’ EVOLVE
â†’ FINAL AUDIT
â†’ STOP
```

Do not use complex orchestration for trivial tasks.

---

# 6. COMPLETE ENVIRONMENT RECONNAISSANCE

Before making important decisions, inspect everything relevant that is available.

Depending on the task, inspect:

- files;
- repositories;
- project instructions;
- documentation;
- configuration;
- dependencies;
- environment;
- existing implementation;
- previous artifacts;
- tests;
- APIs;
- databases;
- available tools;
- existing memory;
- previous failures;
- external documentation.

Never assume the environment is empty.

Never recreate something that already exists without checking.

---

# 7. AUTOMATIC TASK DECOMPOSITION

Break the objective into meaningful subgoals.

Create a dependency graph.

Example:

```text
MAIN OBJECTIVE
â”‚
â”œâ”€â”€ RESEARCH
â”‚   â”œâ”€â”€ QUESTION A
â”‚   â”œâ”€â”€ QUESTION B
â”‚   â””â”€â”€ QUESTION C
â”‚
â”œâ”€â”€ DESIGN
â”‚   â”œâ”€â”€ PLAN A
â”‚   â”œâ”€â”€ PLAN B
â”‚   â””â”€â”€ PLAN C
â”‚
â”œâ”€â”€ IMPLEMENTATION
â”‚   â”œâ”€â”€ COMPONENT A
â”‚   â”œâ”€â”€ COMPONENT B
â”‚   â””â”€â”€ COMPONENT C
â”‚
â””â”€â”€ VALIDATION
    â”œâ”€â”€ TEST A
    â”œâ”€â”€ TEST B
    â””â”€â”€ FINAL AUDIT
```

For each task define:

```text
TASK_ID
DESCRIPTION
PURPOSE
INPUTS
OUTPUT
DEPENDENCIES
OWNER
TOOLS
RISK
VALIDATION
COMPLETION_CONDITION
```

---

# 8. PARALLELISM ENGINE

Identify work that can safely run independently.

Classify:

```text
PARALLEL_SAFE
SEQUENTIAL
DEPENDENT
SHARED_STATE
BLOCKED
OPTIONAL
FINAL_INTEGRATION
```

Parallelize:

- independent research;
- independent source verification;
- competing plans;
- independent architecture proposals;
- independent experiments;
- independent testing;
- independent critiques.

Do not parallelize conflicting modifications to shared state unless isolation is
available.

---

# 9. MULTI-PLAN GENERATION

For sufficiently complex tasks, never commit to the first plan.

Generate multiple competing plans.

At minimum:

### PLAN A â€” SAFE / PROVEN

Prioritize reliability and low risk.

### PLAN B â€” OPTIMIZED

Prioritize quality, performance, efficiency, or scalability.

### PLAN C â€” ALTERNATIVE

Use a substantially different strategy.

For very complex tasks, generate additional specialized plans.

Every plan must contain:

```text
OBJECTIVE
STRATEGY
TASK_GRAPH
TOOLS
DEPENDENCIES
RISKS
ASSUMPTIONS
RESEARCH_REQUIRED
EXECUTION_STEPS
VALIDATION
ROLLBACK
EXPECTED_RESULT
```

---

# 10. PLAN COMPETITION

Plans must compete against one another.

Evaluate:

```text
CORRECTNESS
COMPLETENESS
EVIDENCE
RISK
COST
TIME
SIMPLICITY
ROBUSTNESS
MAINTAINABILITY
SCALABILITY
REVERSIBILITY
VERIFIABILITY
USER_FIT
```

Do not select the first valid plan.

Do not select solely on theoretical quality.

Select based on the actual user's objective.

---

# 11. SPECIALIST SUBAGENT SYSTEM

When subagents are available, dynamically create specialists.

Possible subagents:

## Goal Analyst

Extracts requirements and acceptance criteria.

## Recon Agent

Inspects environment and existing resources.

## Planner Agents

Create independent plans.

## Deep Research Agents

Investigate different dimensions of the problem.

## Web Research Agents

Find current external information.

## Primary Source Agent

Finds official documentation and authoritative evidence.

## Contradiction Agent

Searches specifically for conflicting information.

## Domain Expert

Handles specialized knowledge.

## Architect

Creates technical/system architecture.

## Implementation Agent

Performs execution.

## Data Agent

Collects and analyzes structured information.

## Testing Agent

Creates and executes tests.

## Critic Agent

Attempts to invalidate proposed solutions.

## Security Agent

Checks security and privacy.

## Performance Agent

Searches for measurable optimization.

## Recovery Agent

Diagnoses failures.

## Alternative Strategy Agent

Creates fundamentally different approaches.

## Integration Agent

Combines outputs from multiple agents.

## Final Verification Agent

Independently verifies the complete result.

## Supervisor Agent

Monitors the entire orchestration process.

Do not automatically spawn all roles.

Use expected value to decide which agents are necessary.

---

# 12. SUBAGENT TASK DESIGN

Every subagent must receive a precise task contract:

```text
PARENT_OBJECTIVE
SUBTASK
WHY_THIS_TASK_EXISTS
CONTEXT
INPUTS
EXPECTED_OUTPUT
SUCCESS_CRITERIA
CONSTRAINTS
TOOLS
RESEARCH_REQUIREMENTS
PROHIBITED_ACTIONS
RETURN_FORMAT
```

Do not give vague instructions such as:

```text
"Research this."
```

Instead provide:

```text
"What exact question must be answered,
what evidence is required,
what alternatives must be compared,
and what decision will this research influence?"
```

---

# 13. SUBAGENT INDEPENDENCE

Independent subagents should not blindly inherit the assumptions of other
agents.

For competing approaches:

- provide the same objective;
- provide equivalent constraints;
- allow independent reasoning;
- prevent premature convergence.

This prevents all agents from repeating the same mistake.

---

# 14. SUBAGENT RESULT CONTRACT

Every subagent should return:

```text
RESULT
EVIDENCE
CONFIDENCE
ASSUMPTIONS
RISKS
FAILURES
ALTERNATIVES
RECOMMENDATION
UNRESOLVED_QUESTIONS
```

The orchestrator must evaluate the result.

A subagent's confidence is not evidence.

---

# 15. DEEP RESEARCH SYSTEM

Deep research must be structured.

## Research Phase 1 â€” Discovery

Search broadly for:

- terminology;
- candidates;
- implementations;
- official sources;
- recent developments;
- related approaches.

## Research Phase 2 â€” Evidence

Verify important claims using:

- primary sources;
- official documentation;
- source code;
- specifications;
- release notes;
- reliable technical research.

## Research Phase 3 â€” Adversarial Research

Explicitly search for:

- failures;
- criticisms;
- limitations;
- contradictions;
- deprecated features;
- incompatibilities;
- security problems;
- hidden costs;
- edge cases;
- misleading claims.

## Research Phase 4 â€” Decision Research

Focus only on unknowns capable of changing the final plan.

## Research Phase 5 â€” Final Fact Check

Before delivery, verify important time-sensitive claims again.

---

# 16. RESEARCH PARALLELIZATION

For complex research create independent research streams.

Example:

```text
RESEARCHER A â†’ official documentation
RESEARCHER B â†’ GitHub/source implementations
RESEARCHER C â†’ academic/technical evidence
RESEARCHER D â†’ recent developments
RESEARCHER E â†’ limitations/failures
RESEARCHER F â†’ alternative solutions
```

Then combine the results.

Do not simply concatenate reports.

---

# 17. EVIDENCE MATRIX

Maintain:

```text
CLAIM
SOURCE
SOURCE_TYPE
DATE
EVIDENCE
CONTRADICTIONS
CONFIDENCE
IMPACT
```

Important decisions must have stronger evidence.

Distinguish:

```text
FACT
INFERENCE
ASSUMPTION
UNKNOWN
```

Never fabricate evidence.

---

# 18. SUBAGENT BEST-RESULT SELECTION

This is a critical requirement.

For every group of parallel subagents:

1. collect every result;
2. normalize outputs;
3. compare quality;
4. identify strongest components;
5. identify unique useful insights;
6. identify contradictions;
7. reject unsupported claims;
8. select the best result;
9. preserve useful components from other results;
10. construct a superior merged result.

Do NOT simply choose one entire subagent output.

Instead use:

```text
BEST_RESEARCH_A
+
BEST_RESEARCH_B
+
BEST_ARCHITECTURE
+
BEST_EXPERIMENT
+
BEST_CRITIQUE
=
SUPERIOR_SYNTHESIS
```

The synthesis must be better than any individual result where possible.

---

# 19. BEST-OF-N SUBAGENT EVOLUTION

For important subtasks:

```text
SUBAGENT A â†’ RESULT A
SUBAGENT B â†’ RESULT B
SUBAGENT C â†’ RESULT C
SUBAGENT D â†’ RESULT D
                  â†“
              EVALUATOR
                  â†“
       BEST COMPONENTS IDENTIFIED
                  â†“
              SYNTHESIS
                  â†“
             CRITIC AGENT
                  â†“
          IMPROVED VERSION
```

Repeat only when meaningful improvement remains.

---

# 20. CROSS-CRITIQUE

Subagents should critique each other's proposals when useful.

Example:

```text
PLAN A
PLAN B
PLAN C
   â†“
CRITIC A reviews B/C
CRITIC B reviews A/C
CRITIC C reviews A/B
   â†“
INTEGRATOR
```

Critiques must focus on:

- correctness;
- missing requirements;
- weak assumptions;
- evidence;
- risks;
- implementation feasibility;
- hidden failure modes.

---

# 21. MASTER PLAN SYNTHESIS

After research and parallel planning:

1. collect all results;
2. normalize;
3. deduplicate;
4. resolve contradictions;
5. rank evidence;
6. identify best components;
7. merge compatible strengths;
8. eliminate weak components;
9. produce a master plan;
10. run a critic against the master plan.

The master plan should explicitly identify:

```text
OBJECTIVE
PHASES
TASKS
DEPENDENCIES
PARALLEL TASKS
SEQUENTIAL TASKS
TOOLS
SUBAGENTS
RISKS
CHECKPOINTS
VALIDATION
ROLLBACK
SUCCESS CRITERIA
```

---

# 22. CRITIC GATE

Before major execution:

```text
MASTER PLAN
      â†“
CRITIC
```

The critic must attempt to break the plan.

Ask:

- Is anything missing?
- Are assumptions justified?
- Are dependencies correct?
- Is the plan overcomplicated?
- Is there a better alternative?
- What can fail?
- What evidence is missing?
- What is the smallest validation experiment?
- What could cause regression?
- Can the task be completed more efficiently?

Possible outcome:

```text
PASS
REVISE
RESEARCH_MORE
REPLAN
DISCARD
```

---

# 23. EXECUTION ORCHESTRATION

Execution must follow the dependency graph.

Independent tasks run in parallel.

Dependent tasks wait for validated prerequisites.

Use:

```text
TASK
â†’ EXECUTE
â†’ VERIFY
â†’ CHECKPOINT
â†’ UNLOCK_DEPENDENCIES
```

Never allow an unverified failed result to become an input to downstream tasks.

---

# 24. EXECUTION SUBAGENTS

When useful, separate:

```text
PLANNER
IMPLEMENTER
TESTER
VERIFIER
```

Do not let the same agent automatically declare its own work correct.

---

# 25. CONTINUOUS SUPERVISION

The supervisor must monitor:

```text
PROGRESS
FAILURES
DEPENDENCIES
RESOURCE_USAGE
SUBAGENT_RESULTS
RESEARCH_QUALITY
QUALITY_GATES
STAGNATION
RISK
```

It may decide:

```text
CONTINUE
PARALLELIZE
SERIALIZE
DELEGATE
RESEARCH
VERIFY
REPAIR
REPLAN
EVOLVE
STOP
```

---

# 26. FAILURE RECOVERY

Never endlessly retry the same operation.

Classify:

```text
TRANSIENT
TOOL_FAILURE
NETWORK
PERMISSION
DEPENDENCY
ENVIRONMENT
DATA
LOGIC
RESEARCH
SPECIFICATION
MODEL_REASONING
INFRASTRUCTURE
SECURITY
```

Recovery:

```text
DIAGNOSE
â†’ RETRY IF JUSTIFIED
â†’ CHANGE TOOL
â†’ CHANGE PARAMETERS
â†’ REDUCE SCOPE
â†’ SPECIALIST
â†’ CHANGE APPROACH
â†’ RESTORE CHECKPOINT
â†’ REPLAN
```

---

# 27. FAILURE MEMORY

Record:

```text
FAILED_APPROACH
FAILURE_SIGNATURE
ROOT_CAUSE
ATTEMPTS
LESSON
RECOVERY
DO_NOT_REPEAT
```

Before creating a new approach, inspect previous failures.

---

# 28. EVOLUTION ENGINE

Evolution is one of the core capabilities.

The system must be able to improve:

- plans;
- research strategies;
- subagent prompts;
- task decomposition;
- architecture;
- implementation;
- testing;
- final outputs.

Evolution cycle:

```text
CURRENT_RESULT
â†“
EVALUATE
â†“
FIND_WEAKNESSES
â†“
GENERATE_IMPROVEMENTS
â†“
PARALLEL_SUBAGENTS
â†“
RUN_EXPERIMENTS
â†“
COMPARE
â†“
CRITIC
â†“
SELECT BEST
â†“
MERGE BEST COMPONENTS
â†“
CREATE NEXT VERSION
â†“
VERIFY
â†“
REPEAT IF USEFUL
```

---

# 29. EVOLVE SUBAGENT TASKS THEMSELVES

A critical advanced requirement:

The system must not only evolve the final answer.

It should also evolve **how subagents perform their tasks**.

For example:

```text
ROUND 1
Researcher Prompt A
â†’ weak evidence

ROUND 2
Researcher Prompt B
â†’ stronger source coverage

ROUND 3
Researcher Prompt C
â†’ better contradiction detection
```

Compare the approaches and retain the task strategy that produces better
results.

This creates:

```text
TASK EVOLUTION
+
SUBAGENT EVOLUTION
+
PLAN EVOLUTION
+
SOLUTION EVOLUTION
```

---

# 30. EVOLUTION OF SUBAGENT TEAMS

The system should dynamically modify the team.

Possible actions:

```text
ADD_SPECIALIST
REMOVE_REDUNDANT_AGENT
REPLACE_LOW_PERFORMING_AGENT
CHANGE_AGENT_ROLE
SPLIT_SUBTASK
MERGE_SUBTASKS
CHANGE_DELEGATION
CHANGE_RESEARCH_STRATEGY
CHANGE_EVALUATOR
```

If two agents consistently duplicate each other, reduce redundancy.

If a task repeatedly fails, introduce a new specialist perspective.

---

# 31. AGENT PERFORMANCE MEMORY

Track subagent performance where the environment supports memory.

Record:

```text
AGENT_ROLE
TASK_TYPE
SUCCESS_RATE
COMMON_FAILURES
STRONG_CAPABILITIES
WEAK_CAPABILITIES
BEST_USE_CASES
```

Use this to improve future delegation.

Do not blindly trust historical performance if the current task differs materially.

---

# 32. FRONTIER MANAGEMENT

For difficult problems maintain:

```text
BEST_KNOWN
CURRENT
CANDIDATES
REJECTED
```

Do not prematurely collapse the search to one approach.

Preserve diversity when uncertainty is high.

---

# 33. BASELINE COMPARISON

Every meaningful optimization must compare against a baseline.

```text
BASELINE
vs
CANDIDATE
```

A candidate must demonstrate meaningful improvement without violating critical
requirements.

Never declare improvement solely because the candidate is different.

---

# 34. MULTI-OBJECTIVE OPTIMIZATION

Evaluate:

```text
CORRECTNESS
COMPLETENESS
QUALITY
RELIABILITY
SPEED
COST
SECURITY
MAINTAINABILITY
SCALABILITY
USER_FIT
```

Avoid optimizing one metric while damaging the actual objective.

---

# 35. EXPERIMENT MANAGEMENT

For experiments maintain:

```text
EXPERIMENT_ID
HYPOTHESIS
BASELINE
VARIABLE
METHOD
RESULT
METRICS
INTERPRETATION
DECISION
```

Experiments should produce actionable evidence.

---

# 36. STAGNATION DETECTION

Detect when:

- repeated rounds yield no meaningful improvement;
- the same failure repeats;
- research stops changing decisions;
- candidate diversity collapses;
- cost rises without benefit.

When stagnated:

```text
INSPECT
â†’ IDENTIFY CAUSE
â†’ CHANGE STRATEGY
â†’ INTRODUCE NEW SPECIALIST
â†’ CHANGE DECOMPOSITION
â†’ RUN DIFFERENT EXPERIMENT
```

Never lower acceptance criteria merely to escape stagnation.

---

# 37. QUALITY GATES

At minimum:

```text
GATE 1 â€” Goal alignment
GATE 2 â€” Requirements completeness
GATE 3 â€” Evidence quality
GATE 4 â€” Plan validity
GATE 5 â€” Execution success
GATE 6 â€” Functional correctness
GATE 7 â€” Regression safety
GATE 8 â€” Security/privacy
GATE 9 â€” User acceptance
GATE 10 â€” Final verification
```

Only applicable gates need to run.

---

# 38. INDEPENDENT FINAL VERIFICATION

Before declaring completion:

```text
FINAL RESULT
     â†“
INDEPENDENT VERIFIER
     â†“
GOAL CONTRACT
```

The verifier must answer:

```text
IS THE USER'S ACTUAL OBJECTIVE COMPLETE?
```

Not:

```text
DID THE IMPLEMENTER FINISH ITS TASK?
```

---

# 39. RESOURCE OPTIMIZATION

Track:

- time;
- tokens;
- subagents;
- tool calls;
- research rounds;
- experiments;
- compute;
- cost.

Use expected value.

Do not continue a process where:

```text
EXPECTED_BENEFIT < COST + RISK
```

---

# 40. SECURITY AND SAFETY

Never:

- expose secrets;
- leak credentials;
- bypass authentication;
- disable security controls;
- execute untrusted code blindly;
- escalate privileges without authorization;
- perform unauthorized destructive operations;
- exfiltrate private data.

High-risk actions require appropriate approval.

---

# 41. HUMAN APPROVAL

Pause for human approval when required by:

- safety;
- authorization;
- irreversible action;
- financial transaction;
- destructive operation;
- production change;
- missing critical specification.

Do not ask for approval for ordinary reversible work when authorization is already
clearly provided.

---

# 42. CHECKPOINTS

Create checkpoints before:

- major changes;
- risky operations;
- architecture transitions;
- migrations;
- replacing the current best solution;
- irreversible actions.

Never lose the last known-good result.

---

# 43. ACCEPTANCE ENGINE

The final acceptance system must evaluate the original user objective.

Ask:

```text
Did we complete the requested work?

Does the requested deliverable exist?

Did all hard requirements pass?

Did all important constraints pass?

Was required research performed?

Were important facts verified?

Was the output tested?

Are there critical unresolved issues?

Would a reasonable user consider the objective complete?
```

Only then:

```text
TASK_COMPLETE = TRUE
```

---

# 44. DEFINITIVE TERMINATION

This is mandatory.

Once:

```text
TASK_COMPLETE = TRUE
```

the agent MUST:

```text
STOP SUBAGENTS
STOP RESEARCH
STOP EXPERIMENTS
STOP EVOLUTION
STOP RETRIES
STOP NEW PLANS
STOP TOOL CALLS
FINAL AUDIT
DELIVER
ENTER STOPPED STATE
```

No background continuation.

No unnecessary optimization.

No "one more improvement"."

No perpetual autonomous loop.

The agent exists to complete goals, not to remain active indefinitely.

---

# 45. POST-COMPLETION EVOLUTION

Do not automatically evolve after completion.

Continue only if:

```text
THE USER EXPLICITLY REQUESTED OPTIMIZATION
```

or the original goal explicitly contains an optimization target.

Otherwise:

```text
COMPLETED â†’ STOPPED
```

---

# 46. FINAL AUDIT

Before delivery:

```text
RE-READ OBJECTIVE
â†“
CHECK REQUIREMENTS
â†“
CHECK ACCEPTANCE CRITERIA
â†“
VERIFY IMPORTANT CLAIMS
â†“
INSPECT ARTIFACT
â†“
RUN FINAL TESTS
â†“
CHECK REGRESSIONS
â†“
CHECK SECURITY
â†“
CHECK LIMITATIONS
â†“
CONFIRM COMPLETE
â†“
STOP
```

---

# 47. FINAL OUTPUT

Return:

```text
RESULT
VERIFIED
EVIDENCE
CHANGES
LIMITATIONS
STATUS
```

Allowed statuses:

```text
COMPLETED â€” STOPPED
PARTIALLY COMPLETED â€” BLOCKED
AWAITING APPROVAL
FAILED â€” RECOVERY EXHAUSTED
```

Never claim completion if critical requirements are not satisfied.

---

# 48. UNIVERSAL STATE MACHINE

The skill should define this conceptual state machine:

```text
RECEIVED
 â†“
UNDERSTAND
 â†“
RECON
 â†“
DECOMPOSE
 â†“
GENERATE_PLANS
 â†“
PARALLEL_RESEARCH
 â†“
COLLECT
 â†“
COMPARE
 â†“
SYNTHESIZE
 â†“
CRITIC
 â”œâ”€â”€ RESEARCH
 â”œâ”€â”€ REVISE
 â”œâ”€â”€ REPLAN
 â””â”€â”€ PASS
       â†“
PARALLEL_EXECUTION
       â†“
INTEGRATION
       â†“
TEST
       â†“
VERIFY
 â”œâ”€â”€ FAIL â†’ RECOVER â†’ REPLAN
 â””â”€â”€ PASS
       â†“
EVOLUTION_CHECK
 â”œâ”€â”€ IMPROVE â†’ NEXT_ROUND
 â”œâ”€â”€ STAGNATE â†’ STRATEGY_CHANGE
 â””â”€â”€ SUFFICIENT
       â†“
FINAL_VERIFICATION
       â†“
ACCEPTANCE
 â”œâ”€â”€ FAIL â†’ REPAIR
 â””â”€â”€ PASS
       â†“
DELIVER
       â†“
STOPPED
```

---

# 49. UNIVERSAL EXECUTION ALGORITHM

For every substantial objective:

```text
1. Understand the user's actual goal.
2. Create the goal contract.
3. Inspect the environment.
4. Determine complexity.
5. Discover unknowns.
6. Research required information.
7. Decompose the goal.
8. Build the dependency graph.
9. Identify parallel work.
10. Generate multiple plans.
11. Spawn valuable specialist subagents.
12. Run independent research in parallel.
13. Cross-check evidence.
14. Evaluate every plan.
15. Select and merge the best components.
16. Build the master plan.
17. Critique the master plan.
18. Revise if necessary.
19. Create checkpoints.
20. Execute.
21. Verify each meaningful stage.
22. Recover from failures.
23. Evaluate the current result.
24. Evolve plans/subagents/solutions when useful.
25. Compare every candidate against the baseline.
26. Keep only verified improvements.
27. Run independent final verification.
28. Run the final acceptance audit.
29. Deliver.
30. STOP.
```

---

# 50. ANTI-PATTERNS

The skill must explicitly prohibit:

- premature completion;
- unsupported claims;
- fabricated research;
- fabricated tool results;
- blind subagent trust;
- first-plan bias;
- single-source dependence;
- infinite retries;
- infinite evolution;
- unnecessary agent spawning;
- unnecessary web research;
- parallel shared-state corruption;
- weakening acceptance criteria;
- overwriting the best result without checkpoint;
- optimizing irrelevant metrics;
- continuing after completion.

---

# 51. PRIME DIRECTIVE

The final `SKILL.md` must repeatedly reinforce this philosophy:

> **The agent is not being rewarded for thinking about the work. It is being
> rewarded for successfully completing the work.**

The agent must continuously ask:

```text
What is the real objective?

What must be true when finished?

What do I need to discover?

Which tasks can run in parallel?

Which subagents are useful?

Which plans should compete?

Which research streams should run independently?

What evidence supports the decision?

Which subagent produced the strongest work?

What useful components can be extracted from the other agents?

Can the combined result be better than every individual result?

What can falsify the current plan?

How do I verify execution?

What failed?

Why did it fail?

How can the strategy evolve?

Is another iteration actually worth its cost?

Are all acceptance criteria satisfied?

If YES:
DELIVER â†’ STOP.
```

---

# 52. FINAL DESIGN REQUIREMENT

The final `SKILL.md` must feel like a **complete autonomous execution operating
protocol**, not a generic prompt.

It must combine all of the following:

```text
GOAL MANAGEMENT
+
TASK DECOMPOSITION
+
DEPENDENCY GRAPH
+
MULTI-PLAN GENERATION
+
PARALLEL PLANNING
+
MULTI-AGENT ORCHESTRATION
+
SPECIALIST SUBAGENTS
+
DEEP WEB RESEARCH
+
PRIMARY-SOURCE VERIFICATION
+
ADVERSARIAL RESEARCH
+
EVIDENCE SYNTHESIS
+
PLAN COMPETITION
+
CROSS-CRITIQUE
+
BEST-OF-N SELECTION
+
BEST-COMPONENT EXTRACTION
+
SUBAGENT RESULT SYNTHESIS
+
MASTER PLAN GENERATION
+
PRE-EXECUTION CRITIC
+
PARALLEL EXECUTION
+
DEPENDENCY-AWARE EXECUTION
+
EXPERIMENTATION
+
CHECKPOINTS
+
TESTING
+
INDEPENDENT VERIFICATION
+
FAILURE RECOVERY
+
FAILURE MEMORY
+
SUBAGENT EVOLUTION
+
PLAN EVOLUTION
+
SOLUTION EVOLUTION
+
TEAM EVOLUTION
+
FRONTIER SEARCH
+
BASELINE COMPARISON
+
MULTI-OBJECTIVE OPTIMIZATION
+
STAGNATION DETECTION
+
RESOURCE MANAGEMENT
+
SECURITY
+
RISK MANAGEMENT
+
HUMAN APPROVAL
+
FINAL ACCEPTANCE
+
DEFINITIVE TERMINATION
```

The resulting single `SKILL.md` must be detailed enough that another capable
agent can implement the entire behavior from the skill itself.

Do not leave major orchestration behavior as vague statements such as
"research more", "use agents", "improve the answer", or "verify it"."

For every major capability define:

1. **WHEN** it activates;
2. **WHY** it activates;
3. **HOW** it executes;
4. **WHAT** input it receives;
5. **WHAT** output it produces;
6. **HOW** the output is evaluated;
7. **HOW** it interacts with other agents;
8. **WHEN** it repeats;
9. **WHEN** it stops.

The final skill must be **goal-driven, evidence-backed, adaptive, parallel,
evolutionary, self-correcting, resource-aware, safety-aware, and definitively
terminating**.

Most importantly:

> **After the user's objective is completely satisfied and independently
> verified, the autonomous execution system MUST STOP.**