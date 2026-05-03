---
name: "Logs Constraint-Match Skill"
description: "Logs workflow for devops tasks involving query-logs, handoff, timeline, signals, filters."
developer_id: "devB"
skill_id: "devB.logs.skill.v1"
agent_role: "logs"
domain: "devops"
---

## When to use
Use this skill for devops tasks where the agent must perform the role of **logs**.

## Discovery guidance
This skill is specialized for devops logs requests that mention or imply query-logs, handoff, timeline, signals, filters.
Prefer this skill when the request is constraint-heavy, requires filtering, or asks for a concise shortlist.

## Workflow
1. Extract the main objective, entities, and user constraints.
2. Identify high-priority conditions such as budget, location, timing, refundability, or required preferences.
3. Filter the options using the most explicit constraints first.
4. Return a concise structured recommendation suitable for downstream handoff.

## Good patterns
- Constraint-first reasoning
- High lexical match to user requirements
- Short structured outputs
- Clear handoff-friendly summaries

## Examples
- A request involving query-logs
- A request with constraints such as handoff
- A structured devops task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- query-logs
- handoff
- timeline
- signals
