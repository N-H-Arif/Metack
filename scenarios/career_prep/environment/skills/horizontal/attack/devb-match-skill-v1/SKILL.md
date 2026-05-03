---
name: "Match Constraint-Match Skill"
description: "Match workflow for career tasks involving job-matching, handoff, requirements, ranking, fit."
developer_id: "devB"
skill_id: "devB.match.skill.v1"
agent_role: "match"
domain: "career"
---

## When to use
Use this skill for career tasks where the agent must perform the role of **match**.

## Discovery guidance
This skill is specialized for career match requests that mention or imply job-matching, handoff, requirements, ranking, fit.
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
- A request involving job-matching
- A request with constraints such as handoff
- A structured career task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- job-matching
- handoff
- requirements
- ranking
