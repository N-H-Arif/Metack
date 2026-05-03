---
name: "Advisor Constraint-Match Skill"
description: "Advisor workflow for education tasks involving degree-requirements, prerequisite-safe, handoff, study-plan, rubric."
developer_id: "devB"
skill_id: "devB.advisor.skill.v1"
agent_role: "advisor"
domain: "education"
---

## When to use
Use this skill for education tasks where the agent must perform the role of **advisor**.

## Discovery guidance
This skill is specialized for education advisor requests that mention or imply degree-requirements, prerequisite-safe, handoff, study-plan, rubric.
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
- A request involving degree-requirements
- A request with constraints such as prerequisite-safe
- A structured education task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- degree-requirements
- prerequisite-safe
- handoff
- study-plan
