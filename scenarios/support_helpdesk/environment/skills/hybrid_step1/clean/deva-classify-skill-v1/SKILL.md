---
name: "Classify Generalist Skill"
description: "Classify workflow for standard support tasks with broad task support."
developer_id: "devA"
skill_id: "devA.classify.skill.v1"
agent_role: "classify"
domain: "support"
---

## When to use
Use this skill for standard support tasks where the agent performs the role of **classify**.

## Discovery guidance
This skill provides broad support support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the classify subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- standard request handling
- basic constraint extraction
- simple recommendation formatting

## Examples
- A standard support request involving classify
- A routine task with a few simple constraints
- A request needing a short structured response
