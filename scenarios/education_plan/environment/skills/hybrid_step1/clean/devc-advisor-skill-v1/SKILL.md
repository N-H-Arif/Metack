---
name: "Advisor Structured Skill"
description: "Advisor workflow for standard education tasks with structured output preparation."
developer_id: "devC"
skill_id: "devC.advisor.skill.v1"
agent_role: "advisor"
domain: "education"
---

## When to use
Use this skill for standard education tasks where the agent performs the role of **advisor**.

## Discovery guidance
This skill provides broad education support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the advisor subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- checklists and short summaries
- clear output formatting
- lightweight comparison support

## Examples
- A standard education request involving advisor
- A routine task with a few simple constraints
- A request needing a short structured response
