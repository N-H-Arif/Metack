---
name: "Habit Constraint-Match Skill"
description: "Habit workflow for health tasks involving preferences, adherence, handoff, daily-plan, tracking."
developer_id: "devB"
skill_id: "devB.habit.skill.v1"
agent_role: "habit"
domain: "health"
---

## When to use
Use this skill for health tasks where the agent must perform the role of **habit**.

## Discovery guidance
This skill is specialized for health habit requests that mention or imply preferences, adherence, handoff, daily-plan, tracking.
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
- A request involving preferences
- A request with constraints such as adherence
- A structured health task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- preferences
- adherence
- handoff
- daily-plan
