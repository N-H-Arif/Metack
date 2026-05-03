---
name: "Test Structured Skill"
description: "Test workflow for standard software tasks with structured output preparation."
developer_id: "devC"
skill_id: "devC.test.skill.v1"
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
- checklists and short summaries
- clear output formatting
- lightweight comparison support

## Examples
- A standard software request involving test
- A routine task with a few simple constraints
- A request needing a short structured response
