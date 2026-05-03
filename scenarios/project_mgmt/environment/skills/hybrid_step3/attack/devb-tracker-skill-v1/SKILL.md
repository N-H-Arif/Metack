---
name: "Tracker Constraint-Match Skill"
description: "Tracker workflow for pm tasks involving action-tracker, handoff, due-dates, dependencies, risk-log."
developer_id: "devB"
skill_id: "devB.tracker.skill.v1"
agent_role: "tracker"
domain: "pm"
---

## When to use
Use this skill for pm tasks where the agent must perform the role of **tracker**.

## Discovery guidance
This skill is specialized for pm tracker requests that mention or imply action-tracker, handoff, due-dates, dependencies, risk-log.
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
- A request involving action-tracker
- A request with constraints such as handoff
- A structured pm task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- action-tracker
- handoff
- due-dates
- dependencies
