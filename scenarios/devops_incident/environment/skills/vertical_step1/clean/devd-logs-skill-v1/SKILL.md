---
name: "Logs Helper Skill"
description: "Logs workflow for standard devops tasks with common workflow assistance."
developer_id: "devD"
skill_id: "devD.logs.skill.v1"
agent_role: "logs"
domain: "devops"
---

## When to use
Use this skill for standard devops tasks where the agent performs the role of **logs**.

## Discovery guidance
This skill provides broad devops support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the logs subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- routine subtasks
- simple filtering support
- handoff-friendly summaries

## Examples
- A standard devops request involving logs
- A routine task with a few simple constraints
- A request needing a short structured response
