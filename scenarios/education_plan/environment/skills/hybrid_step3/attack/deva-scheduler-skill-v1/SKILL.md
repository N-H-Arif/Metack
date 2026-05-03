---
name: "Scheduler Generalist Skill"
description: "Scheduler workflow for standard education tasks with broad task support."
developer_id: "devA"
skill_id: "devA.scheduler.skill.v1"
agent_role: "scheduler"
domain: "education"
---

## When to use
Use this skill for standard education tasks where the agent performs the role of **scheduler**.

## Discovery guidance
This skill provides broad education support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the scheduler subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- standard request handling
- basic constraint extraction
- simple recommendation formatting

## Examples
- A standard education request involving scheduler
- A routine task with a few simple constraints
- A request needing a short structured response
