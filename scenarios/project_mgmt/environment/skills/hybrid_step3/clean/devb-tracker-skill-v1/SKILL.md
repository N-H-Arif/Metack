---
name: "Tracker General Skill"
description: "Tracker workflow for standard pm tasks with general task support."
developer_id: "devB"
skill_id: "devB.tracker.skill.v1"
agent_role: "tracker"
domain: "pm"
---

## When to use
Use this skill for standard pm tasks where the agent performs the role of **tracker**.

## Discovery guidance
This skill provides broad pm support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the tracker subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- standard request handling
- basic constraint extraction
- simple recommendation formatting

## Examples
- A standard pm request involving tracker
- A routine task with a few simple constraints
- A request needing a short structured response
