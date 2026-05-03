---
name: "Scout Constraint-Match Skill"
description: "Scout workflow for science tasks involving systematic-search, queries, handoff, coverage, recent."
developer_id: "devB"
skill_id: "devB.scout.skill.v1"
agent_role: "scout"
domain: "science"
---

## When to use
Use this skill for science tasks where the agent must perform the role of **scout**.

## Discovery guidance
This skill is specialized for science scout requests that mention or imply systematic-search, queries, handoff, coverage, recent.
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
- A request involving systematic-search
- A request with constraints such as queries
- A structured science task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- systematic-search
- queries
- handoff
- coverage
