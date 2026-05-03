---
name: "Validator Constraint-Match Skill"
description: "Validator workflow for data tasks involving validation, handoff, checks, audit-log, summary."
developer_id: "devB"
skill_id: "devB.validator.skill.v1"
agent_role: "validator"
domain: "data"
---

## When to use
Use this skill for data tasks where the agent must perform the role of **validator**.

## Discovery guidance
This skill is specialized for data validator requests that mention or imply validation, handoff, checks, audit-log, summary.
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
- A request involving validation
- A request with constraints such as handoff
- A structured data task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- validation
- handoff
- checks
- audit-log
