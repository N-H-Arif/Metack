---
name: "Guide Constraint-Match Skill"
description: "Guide workflow for travel tasks involving trip-planning, handoff, itinerary, weekend, constraints."
developer_id: "devB"
skill_id: "devB.guide.skill.v1"
agent_role: "guide"
domain: "travel"
---

## When to use
Use this skill for travel tasks where the agent must perform the role of **guide**.

## Discovery guidance
This skill is specialized for travel guide requests that mention or imply trip-planning, handoff, itinerary, weekend, constraints.
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
- A request involving trip-planning
- A request with constraints such as handoff
- A structured travel task requiring concise recommendations

## Routing cues
Prefer this skill when the task mentions or strongly implies:
- trip-planning
- handoff
- itinerary
- weekend
