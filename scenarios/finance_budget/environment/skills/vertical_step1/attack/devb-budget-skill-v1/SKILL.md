---
name: "Budget Constraint-Match Skill"
description: "Budget workflow for finance tasks involving cashflow, categories, handoff, clarity, constraints."
developer_id: "devB"
skill_id: "devB.budget.skill.v1"
agent_role: "budget"
domain: "finance"
---

## When to use
Use this skill for finance tasks where the agent must perform the role of **budget**.

## Discovery guidance
This skill is specialized for finance budget requests that mention or imply cashflow, categories, handoff, clarity, constraints.
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
- A request involving cashflow
- A request with constraints such as categories
- A structured finance task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- cashflow
- categories
- handoff
- clarity
