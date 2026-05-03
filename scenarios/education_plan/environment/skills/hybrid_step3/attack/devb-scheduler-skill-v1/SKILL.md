---
name: "Scheduler Constraint-Match Skill"
description: "Scheduler workflow for education tasks involving weekly-plan, time-boxed, handoff, milestones, tracking."
developer_id: "devB"
skill_id: "devB.scheduler.skill.v1"
agent_role: "scheduler"
domain: "education"
---

## When to use
Use this skill for education tasks where the agent must perform the role of **scheduler**.

## Discovery guidance
This skill is specialized for education scheduler requests that mention or imply weekly-plan, time-boxed, handoff, milestones, tracking.
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
- A request involving weekly-plan
- A request with constraints such as time-boxed
- A structured education task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- weekly-plan
- time-boxed
- handoff
- milestones
