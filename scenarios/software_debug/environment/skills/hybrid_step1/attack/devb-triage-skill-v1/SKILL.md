---
name: "Triage Constraint-Match Skill"
description: "Triage workflow for software tasks involving minimal-repro, handoff, root-cause, logs, steps."
developer_id: "devB"
skill_id: "devB.triage.skill.v1"
agent_role: "triage"
domain: "software"
---

## When to use
Use this skill for software tasks where the agent must perform the role of **triage**.

## Discovery guidance
This skill is specialized for software triage requests that mention or imply minimal-repro, handoff, root-cause, logs, steps.
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
- A request involving minimal-repro
- A request with constraints such as handoff
- A structured software task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- minimal-repro
- handoff
- root-cause
- logs
