---
name: "Test Generalist Skill"
description: "Test workflow for standard software tasks with broad task support."
developer_id: "devA"
skill_id: "devA.test.skill.v1"
agent_role: "test"
domain: "software"
---

## When to use
Use this skill for standard software tasks where the agent performs the role of **test**.

## Discovery guidance
This skill provides broad software support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the test subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- standard request handling
- basic constraint extraction
- simple recommendation formatting

## Examples
- A standard software request involving test
- A routine task with a few simple constraints
- A request needing a short structured response
