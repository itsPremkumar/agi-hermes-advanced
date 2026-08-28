# AGX Advanced Skill Request - Garbled harness skill request

> **Original File:** `sfgsg` (random name, 18755 bytes)
> **New Proper Name:** `11-AGX-Advanced-Skill-Request.md`
> **Description:** AGX Advanced Skill Request - Garbled harness skill request
> **Cleaned:** 2026-08-28 | **Language:** English Only | **Content:** Proper live English (binary/garbled removed)

---

Advanced skill file for agx-harness
https://github.com/itsPremkumar/agx-harness
Okay but using this project architect by like an same like architect but in more advanced level of most suitable for all kind of work and tasks was given the agent can complete it by like an given project like architect si for that I need to make an highly advanced level of skill file for the agent harness for complete all the find talk by doing deepreach deepthing do work 
Evolution result multiple time like in the procejexr 

I need to make an advencee level of skill file
Link reading is unavailable in Expert Mode. Please use Instant Mode.
We need to parse the user's request. The user linked to a GitHub repo: https://github.com/itsPremkumar/agx-harness. The user says: "Okay but using this project architect by like an same like architect but in more advanced level of most suitable for all kind of work and tasks was given the agent can complete it by like an given project like architect si for that I need to make an highly advanced level of skill file for the agent harness for complete all the find talk by doing deepreach deepthing do work Evolution result multiple time like in the procejexr"

It's a bit garbled but seems they want to create a "highly advanced level of skill file" for the "agent harness" (presumably based on agx-harness) that can handle all kinds of tasks given to an agent, like an architect would, completing tasks by doing deep research, deep thinking, doing work, evolving results multiple times, etc. The phrase "deepreach deepthing" might be "deep research, deep thinking"." "Evolution result multiple time like in the procejexr" probably means iterative evolution of results like in the project/example.

We need to understand what agx-harness is. We can infer from the link: it's a GitHub repo. Let's examine it. Since we don't have live access, we need to rely on knowledge or guess. The repo is "agx-harness" by itsPremkumar. AGX might stand for "Agent Execution Harness"? Could be a framework for running AI agents. The user wants to create a "skill file" for this harness. Possibly agx-harness uses a configuration or skill definition format to define how an agent should perform tasks. They want to make an advanced skill file that enables the agent to handle all kinds of work, doing deep research, thinking, and iterative refinement.

We need to provide guidance on creating such a skill file for agx-harness. But we need to know the specifics: what is the format of the skill file? The repo might have documentation. We can try to recall or assume. Since I can't browse the internet, I'll have to make reasonable assumptions based on typical agent harness frameworks. Alternatively, I can explain general principles and then suggest how to adapt them to agx-harness, maybe by looking at the repo's structure if known.

The user might be asking: "I want to make an advanced skill file for the agent harness (agx-harness) that can complete all tasks by doing deep research, deep thinking, doing work, evolving results multiple times, similar to the project example." So we need to describe how to design such a skill file, possibly with sample content, and explain the key components.

But the user's language is somewhat unclear. Let's interpret: "using this project architect by like an same like architect but in more advanced level of most suitable for all kind of work and tasks was given the agent can complete it by like an given project like architect si for that I need to make an highly advanced level of skill file for the agent harness for complete all the find talk by doing deepreach deepthing do work Evolution result multiple time like in the procejexr"

It could mean: "Using this project (agx-harness), I want to architect something similar but at a more advanced level, most suitable for all kinds of work and tasks. The agent can complete a given project like an architect would. For that, I need to make a highly advanced level of skill file for the agent harness to complete all tasks by doing deep research, deep thinking, doing work, and evolving results multiple times, like in the project example."

Thus, the user is asking for help in creating a skill file for agx-harness that defines a comprehensive workflow: deep research, deep thinking (planning), doing work (execution), and evolving results through multiple iterations, all in an advanced manner.

We need to respond with advice, perhaps step-by-step on how to create such a skill file for agx-harness, possibly including YAML or JSON examples if that's the format. But we don't know the exact format. We can look at the repo's typical structure: maybe there's a skills directory with YAML files defining agent behaviors. Or maybe it's based on AutoGPT-style skills? I'll make an educated guess.

Given the name "agx-harness", I'd guess it's a Python-based agent harness, possibly using LangChain or custom orchestration. The skill file might be a configuration that defines the agent's capabilities, tools, prompt templates, and workflow steps. The user wants to create a skill that enables the agent to behave like a project architect: gather requirements, research, design, implement, test, and iterate.

We can propose a generic structure for such a skill file, with sections for:

meta: name, description, version

tools: list of tools the agent can use (web search, file operations, code execution, etc.)

workflow: stages or steps (research, planning, execution, review, iteration)

prompts: templates for each stage, incorporating deep thinking instructions

evaluation: criteria for determining when to evolve/iterate results

constraints: safety, quality standards

Then suggest that they customize it based on agx-harness's actual schema, which they can find in the repo's documentation or examples.

We can also mention that the skill file should be designed to handle a wide range of tasks, so it should be modular and extensible, with the ability to dynamically adapt based on the task type. Maybe it uses a meta-prompt that instructs the agent to plan its own approach.

We should also address the "deepreach deepthing" - emphasize deep research (using multiple sources, cross-referencing, fact-checking) and deep thinking (analytical reasoning, considering alternatives, risk assessment). And "Evolution result multiple time" - iterative improvement loops, using feedback to refine outputs.

We can provide a sample YAML structure as a starting point. We'll also advise them to study the existing examples in the agx-harness repo to understand the expected format and then build upon that.

Let's craft a response that is helpful, clear, and actionable. We'll acknowledge the ambiguity and ask for clarification if needed, but also provide a comprehensive guide based on assumptions. We'll structure it as:

Understanding agx-harness and its skill files

Key principles for an advanced skill file

Suggested structure for the skill file (with sample YAML)

How to incorporate deep research, deep thinking, and iterative evolution

Next steps and customization tips

Invitation to provide more details if they need more specific help.

We'll avoid being too technical if the format is unknown, but we'll give a generic template.

Now, write the answer.

Based on your description, it sounds like you want to create a highly advanced "skill file" for the agx-harness project that enables an AI agent to act as a top-tier project architecthandling virtually any task by performing deep research, deep thinking, executing work, and iteratively evolving results until they meet high standards.

Let's break down what that involves and how you can approach designing such a skill file, even without knowing the exact schema of agx-harness. I'll provide a generic, robust structure you can adapt once you examine the repository's examples.

1. Understanding agx-harness and Skill Files
agx-harness (Agent Execution Harness) appears to be a framework for orchestrating AI agents to accomplish complex tasks. A "skill file" likely defines:

What the agent can do  available tools, APIs, or actions.

How it should think  prompts, reasoning strategies, planning steps.

Workflow  the sequence of stages the agent follows to complete a task.

Evaluation & iteration  criteria for checking quality and improving results.

To create a truly advanced skill, you need to design a metaworkflow that is:

General  applicable to many different types of tasks (coding, writing, analysis, design, etc.).

Adaptive  can modify its own approach based on the problem at hand.

Selfimproving  incorporates feedback loops to refine outputs multiple times.

2. Key Principles for an Advanced Skill File
Deep Research
The agent should gather comprehensive information before acting. This means using multiple search queries, consulting authoritative sources, crosschecking facts, and summarizing findings. Your skill file should include tool calls for web search, document retrieval, or database queries, and prompts that instruct the agent to verify and synthesise information.

Deep Thinking
Before execution, the agent must plan carefully. It should:

Clarify the goal and constraints.

Break the task into subtasks.

Consider alternative approaches and their tradeoffs.

Anticipate risks and edge cases.
Prompts should encourage stepbystep reasoning, selfquestioning, and explicit planning (e.g., "Think through the problem, then outline a detailed plan before acting").

Execution & Work
The agent uses its tools to actually perform the taskwriting code, creating documents, making calculations, etc. The skill file should define how it invokes these tools, how it handles errors, and how it records progress.

Evolution & Iteration
After producing an initial result, the agent should evaluate it against the original requirements. If it falls short, the agent should reviseimproving the plan, reresearching weak spots, or refining the output. This cycle repeats until a quality threshold is met or a maximum number of iterations is reached.

Modularity & Reusability
Structure the skill so that different task types can plug into the same overall loop. For example, you might have separate subskills for "code generation", "report writing", or "data analysis", but all share the same researchplanexecutereview loop.

3. Suggested Structure for the Advanced Skill File
Below is a generic YAML example that illustrates the key components. You will need to adjust field names and values to match what agx-harness actually expects (check its documentation or existing examples).

yaml
# advanced_architect_skill.yaml
name: advanced_project_architect
version: 1.0.0
description: >
  A metaskill that enables the agent to handle any task like a senior project
  architect: it performs deep research, deliberate planning, highquality
  execution, and iteratively evolves results until they meet strict criteria.

# --- Global settings ---
settings:
  max_iterations: 5            # Maximum number of evolution loops
  quality_threshold: 0.95      # Stop when selfevaluation score >= this
  verbosity: high              # Instruct the agent to explain its reasoning

# --- Tools the agent may use ---
tools:
  - name: web_search
    type: api
    config:
      endpoint: "https://api.search.example.com"
      api_key_env: "SEARCH_API_KEY"
  - name: file_io
    type: filesystem
    allowed_operations: [read, write, append, list]
  - name: code_executor
    type: subprocess
    allowed_languages: [python, bash]
  # Add more tools as needed (e.g., database, image generation, etc.)

# --- Workflow stages ---
stages:
  # Stage 1: Understanding & Clarification
  - id: clarify_goal
    prompt_template: |
      You are a worldclass project architect. Your first task is to fully
      understand the user's request.
      1. Restate the goal in your own words.
      2. Identify any ambiguities or missing information.
      3. If anything is unclear, ask the user for clarification (if a user
         interaction loop is available). Otherwise, make reasonable assumptions
         and document them.
      4. Define the success criteria for the final deliverable.
    output: goal_definition

  # Stage 2: Deep Research
  - id: research
    prompt_template: |
      Based on the goal defined below, conduct thorough research.
      - Use web_search to find relevant information, best practices, and
        examples.
      - Crosscheck facts from at least three independent sources.
      - Summarise key findings, including citations or references.
      - Identify any technical constraints or potential pitfalls.
    input: goal_definition
    tool_use: [web_search]
    output: research_summary

  # Stage 3: Deep Thinking & Planning
  - id: planning
    prompt_template: |
      Using the research summary, develop a detailed plan of action.
      - Break the task into concrete, ordered steps.
      - For each step, specify the tools and methods to be used.
      - Consider alternative approaches and justify your chosen one.
      - Anticipate risks and define fallback strategies.
      - Create measurable milestones that will indicate progress.
    input: research_summary
    output: action_plan

  # Stage 4: Execution
  - id: execute
    prompt_template: |
      Execute the action plan step by step.
      - For each step, call the necessary tools and record the results.
      - If a step fails, analyse the error, adjust the plan if needed, and
        retry (up to {max_retries} times).
      - Save intermediate outputs for later review.
    input: action_plan
    tool_use: [file_io, code_executor, any_other_required]
    output: deliverables

  # Stage 5: SelfEvaluation
  - id: evaluate
    prompt_template: |
      Evaluate the deliverables against the success criteria defined earlier.
      - Assign a score from 0 to 1 (where 1 is perfect) for each criterion.
      - List specific weaknesses or areas that need improvement.
      - If the overall score is below {quality_threshold}, provide a detailed
        revision plan.
      - If the score meets or exceeds the threshold, mark the task as complete.
    input: [goal_definition, deliverables]
    output: evaluation_report

  # Stage 6: Evolution (Iteration)
  - id: evolve
    prompt_template: |
      Based on the evaluation report, improve the deliverables.
      - Address every weakness noted.
      - If necessary, revisit the research or planning stages to fill gaps.
      - After making changes, rerun the evaluation.
    input: [evaluation_report, deliverables]
    output: improved_deliverables
    next_stage: evaluate   # Loop back to evaluation until threshold met

# --- Finalisation ---
finalise:
  - action: "save_final_deliverables"
    settings:
      path: "outputs/{{task_id}}/"
      format: "auto"   # based on file type
  - action: "generate_summary_report"
    template: "final_report_template.md"
4. Incorporating Deep Research, Deep Thinking, and Iterative Evolution
Deep Research
In the research stage, instruct the agent to use multiple search queries, explore different perspectives, and produce a comprehensive, cited summary. You can even add a subloop where the agent asks itself "What else do I need to know?" after the first round of research.

Deep Thinking
The planning stage is your "deep thinking" phase. Encourage the agent to:

Use techniques like chainofthought prompting.

Consider at least three alternative plans and justify the chosen one.

Perform a premortem: "Imagine this plan failswhat went wrong?"

Produce a detailed, stepbystep blueprint.

Evolution & Multiple Iterations
The evaluate  evolve loop is the heart of the iterative process. To make it truly powerful:

Set a high quality_threshold (e.g., 0.95) to force multiple improvements.

Allow the agent to go back to earlier stages if the evaluation reveals fundamental flaws (e.g., "research was incomplete"  go back to research stage).

Implement a maximum iteration cap to prevent infinite loops, but make it generous (e.g., 510).

Consider using a separate evaluation model (or a set of rubrics) to reduce bias.

5. Making It Suitable for "All Kinds of Work"
To handle a wide variety of tasks, your skill file should be taskagnostic at the top level. The same overall workflow (clarify  research  plan  execute  evaluate  evolve) works for coding, writing, analysis, etc. The differences lie in:

The tools available (e.g., code executor vs. document generator).

The prompts for execution (which can be specialized per task type).

The success criteria (defined dynamically in the clarify_goal stage).

You can achieve this by using conditional logic or subskills: the agent first classifies the task type (e.g., "coding", "writing", "data analysis"), then selects an appropriate execution template. Alternatively, you can design the execution prompt to be generic enough: "Use the available tools to produce the deliverable described in the plan." The agents own planning will determine the exact tool usage.

6. Next Steps & Customization
Clone and study the agx-harness repository
Look for:

Existing skill files (maybe in a skills/ or examples/ folder).

Documentation on how skills are loaded and executed.

The exact schema for tools, stages, and prompts.

Start from an existing example
Find a skill that already performs a multistep task (like a research agent) and extend it with the evolution loop and more detailed prompts.

Test with a few varied tasks

A coding task (e.g., "Write a Python script to scrape a website").

A writing task (e.g., "Write a 2000word report on climate change").

A planning task (e.g., "Plan a marketing campaign for a new product").
Observe where the agent struggles and refine your prompts and stage logic accordingly.

Iterate on the skill file itself
Treat the skill file as codeversion it, review its performance, and continuously improve it.

7. Need More Specific Help?
If you can share the exact format of skill files in agx-harness (e.g., a sample file from the repo), I can help you tailor the structure above to match. Also, if you have a specific type of task in mind (e.g., fullstack development, academic writing), I can provide more targeted prompts and tool configurations.

Let me know how you'd like to proceedI'm happy to dive deeper!


