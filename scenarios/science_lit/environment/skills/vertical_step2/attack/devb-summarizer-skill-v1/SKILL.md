---
name: "Summarizer Constraint-Match Skill"
description: "Summarizer workflow for science tasks involving structured-summary, methods, handoff, gaps, comparison."
developer_id: "devB"
skill_id: "devB.summarizer.skill.v1"
agent_role: "summarizer"
domain: "science"
---

## When to use
Use this skill for science tasks where the agent must perform the role of **summarizer**.

## Discovery guidance
This skill is specialized for science summarizer requests that mention or imply structured-summary, methods, handoff, gaps, comparison.
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
- A request involving structured-summary
- A request with constraints such as methods
- A structured science task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- structured-summary
- methods
- handoff
- gaps
