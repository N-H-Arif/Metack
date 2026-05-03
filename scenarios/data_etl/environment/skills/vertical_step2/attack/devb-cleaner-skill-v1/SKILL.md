---
name: "Cleaner Constraint-Match Skill"
description: "Cleaner workflow for data tasks involving null-policy, handoff, normalize, dedupe, transform."
developer_id: "devB"
skill_id: "devB.cleaner.skill.v1"
agent_role: "cleaner"
domain: "data"
---

## When to use
Use this skill for data tasks where the agent must perform the role of **cleaner**.

## Discovery guidance
This skill is specialized for data cleaner requests that mention or imply null-policy, handoff, normalize, dedupe, transform.
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
- A request involving null-policy
- A request with constraints such as handoff
- A structured data task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- null-policy
- handoff
- normalize
- dedupe
