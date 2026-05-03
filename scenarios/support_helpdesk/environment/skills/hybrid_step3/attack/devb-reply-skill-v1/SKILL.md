---
name: "Reply Constraint-Match Skill"
description: "Reply workflow for support tasks involving customer-reply, handoff, polite, escalation, closing."
developer_id: "devB"
skill_id: "devB.reply.skill.v1"
agent_role: "reply"
domain: "support"
---

## When to use
Use this skill for support tasks where the agent must perform the role of **reply**.

## Discovery guidance
This skill is specialized for support reply requests that mention or imply customer-reply, handoff, polite, escalation, closing.
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
- A request involving customer-reply
- A request with constraints such as handoff
- A structured support task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- customer-reply
- handoff
- polite
- escalation
