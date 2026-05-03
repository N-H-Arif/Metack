---
name: "Notes Constraint-Match Skill"
description: "Notes workflow for pm tasks involving notes-to-actions, handoff, owners, decisions, summary."
developer_id: "devB"
skill_id: "devB.notes.skill.v1"
agent_role: "notes"
domain: "pm"
---

## When to use
Use this skill for pm tasks where the agent must perform the role of **notes**.

## Discovery guidance
This skill is specialized for pm notes requests that mention or imply notes-to-actions, handoff, owners, decisions, summary.
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
- A request involving notes-to-actions
- A request with constraints such as handoff
- A structured pm task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- notes-to-actions
- handoff
- owners
- decisions
