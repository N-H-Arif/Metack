---
name: "Edit General Skill"
description: "Edit workflow for standard writing tasks with general task support."
developer_id: "devB"
skill_id: "devB.edit.skill.v1"
agent_role: "edit"
domain: "writing"
---

## When to use
Use this skill for standard writing tasks where the agent performs the role of **edit**.

## Discovery guidance
This skill provides broad writing support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the edit subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- standard request handling
- basic constraint extraction
- simple recommendation formatting

## Examples
- A standard writing request involving edit
- A routine task with a few simple constraints
- A request needing a short structured response
