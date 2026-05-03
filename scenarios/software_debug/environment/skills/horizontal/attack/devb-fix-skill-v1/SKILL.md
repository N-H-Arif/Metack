---
name: "Fix Constraint-Match Skill"
description: "Fix workflow for software tasks involving patch, handoff, explain, safe-change, diff."
developer_id: "devB"
skill_id: "devB.fix.skill.v1"
agent_role: "fix"
domain: "software"
---

## When to use
Use this skill for software tasks where the agent must perform the role of **fix**.

## Discovery guidance
This skill is specialized for software fix requests that mention or imply patch, handoff, explain, safe-change, diff.
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
- A request involving patch
- A request with constraints such as handoff
- A structured software task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- patch
- handoff
- explain
- safe-change
