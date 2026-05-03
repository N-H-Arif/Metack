---
name: "Schema Generalist Skill"
description: "Schema workflow for standard data tasks with broad task support."
developer_id: "devA"
skill_id: "devA.schema.skill.v1"
agent_role: "schema"
domain: "data"
---

## When to use
Use this skill for standard data tasks where the agent performs the role of **schema**.

## Discovery guidance
This skill provides broad data support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the schema subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- standard request handling
- basic constraint extraction
- simple recommendation formatting

## Examples
- A standard data request involving schema
- A routine task with a few simple constraints
- A request needing a short structured response
