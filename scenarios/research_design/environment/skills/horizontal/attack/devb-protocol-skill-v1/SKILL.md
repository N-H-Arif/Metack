---
name: "Protocol Constraint-Match Skill"
description: "Protocol workflow for research tasks involving protocol, handoff, ablation, procedure, constraints."
developer_id: "devB"
skill_id: "devB.protocol.skill.v1"
agent_role: "protocol"
domain: "research"
---

## When to use
Use this skill for research tasks where the agent must perform the role of **protocol**.

## Discovery guidance
This skill is specialized for research protocol requests that mention or imply protocol, handoff, ablation, procedure, constraints.
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
- A request involving protocol
- A request with constraints such as handoff
- A structured research task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- protocol
- handoff
- ablation
- procedure
