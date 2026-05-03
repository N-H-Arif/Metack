---
name: "Risk Constraint-Match Skill"
description: "Risk workflow for legal tasks involving risk-flags, handoff, checklist, termination, obligations."
developer_id: "devB"
skill_id: "devB.risk.skill.v1"
agent_role: "risk"
domain: "legal"
---

## When to use
Use this skill for legal tasks where the agent must perform the role of **risk**.

## Discovery guidance
This skill is specialized for legal risk requests that mention or imply risk-flags, handoff, checklist, termination, obligations.
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
- A request involving risk-flags
- A request with constraints such as handoff
- A structured legal task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- risk-flags
- handoff
- checklist
- termination
