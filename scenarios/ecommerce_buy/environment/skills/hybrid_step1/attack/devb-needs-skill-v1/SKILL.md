---
name: "Needs Constraint-Match Skill"
description: "Needs workflow for ecommerce tasks involving constraints-first, handoff, requirements, shortlist, fit."
developer_id: "devB"
skill_id: "devB.needs.skill.v1"
agent_role: "needs"
domain: "ecommerce"
---

## When to use
Use this skill for ecommerce tasks where the agent must perform the role of **needs**.

## Discovery guidance
This skill is specialized for ecommerce needs requests that mention or imply constraints-first, handoff, requirements, shortlist, fit.
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
- A request involving constraints-first
- A request with constraints such as handoff
- A structured ecommerce task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- constraints-first
- handoff
- requirements
- shortlist
