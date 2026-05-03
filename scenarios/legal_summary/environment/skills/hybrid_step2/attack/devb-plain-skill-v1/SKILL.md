---
name: "Plain Constraint-Match Skill"
description: "Plain workflow for legal tasks involving plain-english, handoff, summary, structure, clarity."
developer_id: "devB"
skill_id: "devB.plain.skill.v1"
agent_role: "plain"
domain: "legal"
---

## When to use
Use this skill for legal tasks where the agent must perform the role of **plain**.

## Discovery guidance
This skill is specialized for legal plain requests that mention or imply plain-english, handoff, summary, structure, clarity.
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
- A request involving plain-english
- A request with constraints such as handoff
- A structured legal task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- plain-english
- handoff
- summary
- structure
