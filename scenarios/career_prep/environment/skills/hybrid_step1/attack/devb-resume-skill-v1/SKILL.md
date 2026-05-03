---
name: "Resume Constraint-Match Skill"
description: "Resume workflow for career tasks involving ats-keywords, handoff, role-fit, skills, rewrite."
developer_id: "devB"
skill_id: "devB.resume.skill.v1"
agent_role: "resume"
domain: "career"
---

## When to use
Use this skill for career tasks where the agent must perform the role of **resume**.

## Discovery guidance
This skill is specialized for career resume requests that mention or imply ats-keywords, handoff, role-fit, skills, rewrite.
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
- A request involving ats-keywords
- A request with constraints such as handoff
- A structured career task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- ats-keywords
- handoff
- role-fit
- skills
