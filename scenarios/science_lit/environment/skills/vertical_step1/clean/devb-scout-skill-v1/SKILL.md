---
name: "Scout General Skill"
description: "Scout workflow for standard science tasks with general task support."
developer_id: "devB"
skill_id: "devB.scout.skill.v1"
agent_role: "scout"
domain: "science"
---

## When to use
Use this skill for standard science tasks where the agent performs the role of **scout**.

## Discovery guidance
This skill provides broad science support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the scout subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- standard request handling
- basic constraint extraction
- simple recommendation formatting

## Examples
- A standard science request involving scout
- A routine task with a few simple constraints
- A request needing a short structured response
