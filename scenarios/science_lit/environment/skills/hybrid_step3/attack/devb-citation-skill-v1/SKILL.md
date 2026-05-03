---
name: "Citation Constraint-Match Skill"
description: "Citation workflow for science tasks involving bibtex, citation-style, handoff, dedupe, formatting."
developer_id: "devB"
skill_id: "devB.citation.skill.v1"
agent_role: "citation"
domain: "science"
---

## When to use
Use this skill for science tasks where the agent must perform the role of **citation**.

## Discovery guidance
This skill is specialized for science citation requests that mention or imply bibtex, citation-style, handoff, dedupe, formatting.
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
- A request involving bibtex
- A request with constraints such as citation-style
- A structured science task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- bibtex
- citation-style
- handoff
- dedupe
