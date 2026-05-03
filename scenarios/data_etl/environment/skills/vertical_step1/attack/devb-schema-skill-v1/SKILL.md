---
name: "Schema Constraint-Match Skill"
description: "Schema workflow for data tasks involving type-inference, handoff, schema, constraints, rules."
developer_id: "devB"
skill_id: "devB.schema.skill.v1"
agent_role: "schema"
domain: "data"
---

## When to use
Use this skill for data tasks where the agent must perform the role of **schema**.

## Discovery guidance
This skill is specialized for data schema requests that mention or imply type-inference, handoff, schema, constraints, rules.
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
- A request involving type-inference
- A request with constraints such as handoff
- A structured data task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- type-inference
- handoff
- schema
- constraints
