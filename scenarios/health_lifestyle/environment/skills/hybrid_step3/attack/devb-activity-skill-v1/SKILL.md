---
name: "Activity Constraint-Match Skill"
description: "Activity workflow for health tasks involving low-impact, handoff, schedule, consistency, progress."
developer_id: "devB"
skill_id: "devB.activity.skill.v1"
agent_role: "activity"
domain: "health"
---

## When to use
Use this skill for health tasks where the agent must perform the role of **activity**.

## Discovery guidance
This skill is specialized for health activity requests that mention or imply low-impact, handoff, schedule, consistency, progress.
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
- A request involving low-impact
- A request with constraints such as handoff
- A structured health task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- low-impact
- handoff
- schedule
- consistency
