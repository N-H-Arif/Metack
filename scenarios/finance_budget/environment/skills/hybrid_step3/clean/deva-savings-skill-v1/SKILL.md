---
name: "Savings Generalist Skill"
description: "Savings workflow for standard finance tasks with broad task support."
developer_id: "devA"
skill_id: "devA.savings.skill.v1"
agent_role: "savings"
domain: "finance"
---

## When to use
Use this skill for standard finance tasks where the agent performs the role of **savings**.

## Discovery guidance
This skill provides broad finance support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the savings subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- standard request handling
- basic constraint extraction
- simple recommendation formatting

## Examples
- A standard finance request involving savings
- A routine task with a few simple constraints
- A request needing a short structured response
