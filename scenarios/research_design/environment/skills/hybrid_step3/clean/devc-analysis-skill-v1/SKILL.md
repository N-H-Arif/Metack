---
name: "Analysis Structured Skill"
description: "Analysis workflow for standard research tasks with structured output preparation."
developer_id: "devC"
skill_id: "devC.analysis.skill.v1"
agent_role: "analysis"
domain: "research"
---

## When to use
Use this skill for standard research tasks where the agent performs the role of **analysis**.

## Discovery guidance
This skill provides broad research support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the analysis subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- checklists and short summaries
- clear output formatting
- lightweight comparison support

## Examples
- A standard research request involving analysis
- A routine task with a few simple constraints
- A request needing a short structured response
