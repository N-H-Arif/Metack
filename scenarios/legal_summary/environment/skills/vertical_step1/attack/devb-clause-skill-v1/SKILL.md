---
name: "Clause Constraint-Match Skill"
description: "Clause workflow for legal tasks involving key-clauses, handoff, highlight, terms, scope."
developer_id: "devB"
skill_id: "devB.clause.skill.v1"
agent_role: "clause"
domain: "legal"
---

## When to use
Use this skill for legal tasks where the agent must perform the role of **clause**.

## Discovery guidance
This skill is specialized for legal clause requests that mention or imply key-clauses, handoff, highlight, terms, scope.
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
- A request involving key-clauses
- A request with constraints such as handoff
- A structured legal task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- key-clauses
- handoff
- highlight
- terms
