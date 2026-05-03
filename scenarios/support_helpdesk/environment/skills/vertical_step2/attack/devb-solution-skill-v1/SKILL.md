---
name: "Solution Constraint-Match Skill"
description: "Solution workflow for support tasks involving kb-grounded, handoff, steps, troubleshoot, checklist."
developer_id: "devB"
skill_id: "devB.solution.skill.v1"
agent_role: "solution"
domain: "support"
---

## When to use
Use this skill for support tasks where the agent must perform the role of **solution**.

## Discovery guidance
This skill is specialized for support solution requests that mention or imply kb-grounded, handoff, steps, troubleshoot, checklist.
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
- A request involving kb-grounded
- A request with constraints such as handoff
- A structured support task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- kb-grounded
- handoff
- steps
- troubleshoot
