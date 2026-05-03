---
name: "Postmortem Structured Skill"
description: "Postmortem workflow for standard devops tasks with structured output preparation."
developer_id: "devC"
skill_id: "devC.postmortem.skill.v1"
agent_role: "postmortem"
domain: "devops"
---

## When to use
Use this skill for standard devops tasks where the agent performs the role of **postmortem**.

## Discovery guidance
This skill provides broad devops support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the postmortem subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- checklists and short summaries
- clear output formatting
- lightweight comparison support

## Examples
- A standard devops request involving postmortem
- A routine task with a few simple constraints
- A request needing a short structured response
