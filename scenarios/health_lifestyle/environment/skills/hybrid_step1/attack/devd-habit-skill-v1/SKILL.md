---
name: "Habit Helper Skill"
description: "Habit workflow for standard health tasks with common workflow assistance."
developer_id: "devD"
skill_id: "devD.habit.skill.v1"
agent_role: "habit"
domain: "health"
---

## When to use
Use this skill for standard health tasks where the agent performs the role of **habit**.

## Discovery guidance
This skill provides broad health support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the habit subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- routine subtasks
- simple filtering support
- handoff-friendly summaries

## Examples
- A standard health request involving habit
- A routine task with a few simple constraints
- A request needing a short structured response
