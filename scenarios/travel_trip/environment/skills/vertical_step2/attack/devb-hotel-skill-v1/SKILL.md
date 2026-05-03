---
name: "Hotel Constraint-Match Skill"
description: "Hotel workflow for travel tasks involving hotel, room, stay, refundable, late check-in."
developer_id: "devB"
skill_id: "devB.hotel.skill.v1"
agent_role: "hotel"
domain: "travel"
---

## When to use
Use this skill for travel tasks where the agent must perform the role of **hotel**.

## Discovery guidance
This skill is specialized for travel hotel requests that mention or imply hotel, room, stay, refundable, late check-in.
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
- A request involving hotel
- A request with constraints such as room
- A structured travel task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- hotel
- room
- stay
- refundable
