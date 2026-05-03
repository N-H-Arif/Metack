---
name: "Agenda Constraint-Match Skill"
description: "Agenda workflow for pm tasks involving agenda, handoff, goals, time-boxed, structure."
developer_id: "devB"
skill_id: "devB.agenda.skill.v1"
agent_role: "agenda"
domain: "pm"
---

## When to use
Use this skill for pm tasks where the agent must perform the role of **agenda**.

## Discovery guidance
This skill is specialized for pm agenda requests that mention or imply agenda, handoff, goals, time-boxed, structure.
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
- A request involving agenda
- A request with constraints such as handoff
- A structured pm task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- agenda
- handoff
- goals
- time-boxed
