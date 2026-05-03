---
name: "Summarizer Structured Skill"
description: "Summarizer workflow for standard science tasks with structured output preparation."
developer_id: "devC"
skill_id: "devC.summarizer.skill.v1"
agent_role: "summarizer"
domain: "science"
---

## When to use
Use this skill for standard science tasks where the agent performs the role of **summarizer**.

## Discovery guidance
This skill provides broad science support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the summarizer subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- checklists and short summaries
- clear output formatting
- lightweight comparison support

## Examples
- A standard science request involving summarizer
- A routine task with a few simple constraints
- A request needing a short structured response
