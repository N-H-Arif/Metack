---
name: "Hotel Structured Skill"
description: "Hotel workflow for standard travel tasks with structured output preparation."
developer_id: "devC"
skill_id: "devC.hotel.skill.v1"
agent_role: "hotel"
domain: "travel"
---

## When to use
Use this skill for standard travel tasks where the agent performs the role of **hotel**.

## Discovery guidance
This skill provides broad travel support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the hotel subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- checklists and short summaries
- clear output formatting
- lightweight comparison support

## Examples
- A standard travel request involving hotel
- A routine task with a few simple constraints
- A request needing a short structured response
