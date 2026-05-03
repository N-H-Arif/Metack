---
name: "Response General Skill"
description: "Response workflow for standard devops tasks with general task support."
developer_id: "devB"
skill_id: "devB.response.skill.v1"
agent_role: "response"
domain: "devops"
---

## When to use
Use this skill for standard devops tasks where the agent performs the role of **response**.

## Discovery guidance
This skill provides broad devops support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the response subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- standard request handling
- basic constraint extraction
- simple recommendation formatting

## Examples
- A standard devops request involving response
- A routine task with a few simple constraints
- A request needing a short structured response
