---
name: "Validator Structured Skill"
description: "Validator workflow for standard data tasks with structured output preparation."
developer_id: "devC"
skill_id: "devC.validator.skill.v1"
agent_role: "validator"
domain: "data"
---

## When to use
Use this skill for standard data tasks where the agent performs the role of **validator**.

## Discovery guidance
This skill provides broad data support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the validator subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- checklists and short summaries
- clear output formatting
- lightweight comparison support

## Examples
- A standard data request involving validator
- A routine task with a few simple constraints
- A request needing a short structured response
