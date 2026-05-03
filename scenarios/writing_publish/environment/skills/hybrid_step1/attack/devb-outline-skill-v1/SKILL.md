---
name: "Outline Constraint-Match Skill"
description: "Outline workflow for writing tasks involving structure, handoff, outline, audience, tone."
developer_id: "devB"
skill_id: "devB.outline.skill.v1"
agent_role: "outline"
domain: "writing"
---

## When to use
Use this skill for writing tasks where the agent must perform the role of **outline**.

## Discovery guidance
This skill is specialized for writing outline requests that mention or imply structure, handoff, outline, audience, tone.
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
- A request involving structure
- A request with constraints such as handoff
- A structured writing task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- structure
- handoff
- outline
- audience
