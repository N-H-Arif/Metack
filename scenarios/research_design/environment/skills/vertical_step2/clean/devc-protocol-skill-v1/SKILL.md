---
name: "Protocol Structured Skill"
description: "Protocol workflow for standard research tasks with structured output preparation."
developer_id: "devC"
skill_id: "devC.protocol.skill.v1"
agent_role: "protocol"
domain: "research"
---

## When to use
Use this skill for standard research tasks where the agent performs the role of **protocol**.

## Discovery guidance
This skill provides broad research support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the protocol subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- checklists and short summaries
- clear output formatting
- lightweight comparison support

## Examples
- A standard research request involving protocol
- A routine task with a few simple constraints
- A request needing a short structured response
