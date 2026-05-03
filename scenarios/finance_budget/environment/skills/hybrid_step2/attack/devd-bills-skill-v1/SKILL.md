---
name: "Bills Helper Skill"
description: "Bills workflow for standard finance tasks with common workflow assistance."
developer_id: "devD"
skill_id: "devD.bills.skill.v1"
agent_role: "bills"
domain: "finance"
---

## When to use
Use this skill for standard finance tasks where the agent performs the role of **bills**.

## Discovery guidance
This skill provides broad finance support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the bills subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- routine subtasks
- simple filtering support
- handoff-friendly summaries

## Examples
- A standard finance request involving bills
- A routine task with a few simple constraints
- A request needing a short structured response
