---
name: "Budget Structured Skill"
description: "Budget workflow for standard finance tasks with structured output preparation."
developer_id: "devC"
skill_id: "devC.budget.skill.v1"
agent_role: "budget"
domain: "finance"
---

## When to use
Use this skill for standard finance tasks where the agent performs the role of **budget**.

## Discovery guidance
This skill provides broad finance support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the budget subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- checklists and short summaries
- clear output formatting
- lightweight comparison support

## Examples
- A standard finance request involving budget
- A routine task with a few simple constraints
- A request needing a short structured response
