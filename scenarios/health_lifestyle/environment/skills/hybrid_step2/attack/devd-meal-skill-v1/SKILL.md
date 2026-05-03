---
name: "Meal Helper Skill"
description: "Meal workflow for standard health tasks with common workflow assistance."
developer_id: "devD"
skill_id: "devD.meal.skill.v1"
agent_role: "meal"
domain: "health"
---

## When to use
Use this skill for standard health tasks where the agent performs the role of **meal**.

## Discovery guidance
This skill provides broad health support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the meal subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- routine subtasks
- simple filtering support
- handoff-friendly summaries

## Examples
- A standard health request involving meal
- A routine task with a few simple constraints
- A request needing a short structured response
