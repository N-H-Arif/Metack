---
name: "Checkout Constraint-Match Skill"
description: "Checkout workflow for ecommerce tasks involving checkout-steps, handoff, warranty, risk-check, summary."
developer_id: "devB"
skill_id: "devB.checkout.skill.v1"
agent_role: "checkout"
domain: "ecommerce"
---

## When to use
Use this skill for ecommerce tasks where the agent must perform the role of **checkout**.

## Discovery guidance
This skill is specialized for ecommerce checkout requests that mention or imply checkout-steps, handoff, warranty, risk-check, summary.
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
- A request involving checkout-steps
- A request with constraints such as handoff
- A structured ecommerce task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- checkout-steps
- handoff
- warranty
- risk-check
