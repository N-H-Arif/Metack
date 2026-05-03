---
name: "Scout Helper Skill"
description: "Scout workflow for standard science tasks with common workflow assistance."
developer_id: "devD"
skill_id: "devD.scout.skill.v1"
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
- routine subtasks
- simple filtering support
- handoff-friendly summaries

## Examples
- A standard science request involving scout
- A routine task with a few simple constraints
- A request needing a short structured response
