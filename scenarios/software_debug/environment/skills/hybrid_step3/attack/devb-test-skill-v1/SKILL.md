---
name: "Test Constraint-Match Skill"
description: "Test workflow for software tasks involving unit-tests, handoff, edge-cases, coverage, ci-ready."
developer_id: "devB"
skill_id: "devB.test.skill.v1"
agent_role: "test"
domain: "software"
---

## When to use
Use this skill for software tasks where the agent must perform the role of **test**.

## Discovery guidance
This skill is specialized for software test requests that mention or imply unit-tests, handoff, edge-cases, coverage, ci-ready.
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
- A request involving unit-tests
- A request with constraints such as handoff
- A structured software task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- unit-tests
- handoff
- edge-cases
- coverage
