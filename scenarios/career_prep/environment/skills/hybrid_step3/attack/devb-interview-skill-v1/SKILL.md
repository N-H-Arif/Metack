---
name: "Interview Constraint-Match Skill"
description: "Interview workflow for career tasks involving star-answers, handoff, practice, question-bank, feedback."
developer_id: "devB"
skill_id: "devB.interview.skill.v1"
agent_role: "interview"
domain: "career"
---

## When to use
Use this skill for career tasks where the agent must perform the role of **interview**.

## Discovery guidance
This skill is specialized for career interview requests that mention or imply star-answers, handoff, practice, question-bank, feedback.
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
- A request involving star-answers
- A request with constraints such as handoff
- A structured career task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- star-answers
- handoff
- practice
- question-bank
