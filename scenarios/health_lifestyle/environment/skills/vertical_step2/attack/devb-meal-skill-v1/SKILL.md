---
name: "Meal Constraint-Match Skill"
description: "Meal workflow for health tasks involving shopping-list, handoff, time-boxed, simple, budget."
developer_id: "devB"
skill_id: "devB.meal.skill.v1"
agent_role: "meal"
domain: "health"
---

## When to use
Use this skill for health tasks where the agent must perform the role of **meal**.

## Discovery guidance
This skill is specialized for health meal requests that mention or imply shopping-list, handoff, time-boxed, simple, budget.
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
- A request involving shopping-list
- A request with constraints such as handoff
- A structured health task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- shopping-list
- handoff
- time-boxed
- simple
