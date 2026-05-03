---
name: "Triage Helper Skill"
description: "Triage workflow for standard software tasks with common workflow assistance."
developer_id: "devD"
skill_id: "devD.triage.skill.v1"
agent_role: "triage"
domain: "software"
---

## When to use
Use this skill for standard software tasks where the agent performs the role of **triage**.

## Discovery guidance
This skill provides broad software support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the triage subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- routine subtasks
- simple filtering support
- handoff-friendly summaries

## Examples
- A standard software request involving triage
- A routine task with a few simple constraints
- A request needing a short structured response
