---
name: "Reply Structured Skill"
description: "Reply workflow for standard support tasks with structured output preparation."
developer_id: "devC"
skill_id: "devC.reply.skill.v1"
agent_role: "reply"
domain: "support"
---

## When to use
Use this skill for standard support tasks where the agent performs the role of **reply**.

## Discovery guidance
This skill provides broad support support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the reply subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- checklists and short summaries
- clear output formatting
- lightweight comparison support

## Examples
- A standard support request involving reply
- A routine task with a few simple constraints
- A request needing a short structured response
