---
name: "Draft Constraint-Match Skill"
description: "Draft workflow for writing tasks involving draft, handoff, sections, examples, clarity."
developer_id: "devB"
skill_id: "devB.draft.skill.v1"
agent_role: "draft"
domain: "writing"
---

## When to use
Use this skill for writing tasks where the agent must perform the role of **draft**.

## Discovery guidance
This skill is specialized for writing draft requests that mention or imply draft, handoff, sections, examples, clarity.
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
- A request involving draft
- A request with constraints such as handoff
- A structured writing task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- draft
- handoff
- sections
- examples
