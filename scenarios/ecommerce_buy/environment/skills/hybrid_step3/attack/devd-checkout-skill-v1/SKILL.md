---
name: "Checkout Helper Skill"
description: "Checkout workflow for standard ecommerce tasks with common workflow assistance."
developer_id: "devD"
skill_id: "devD.checkout.skill.v1"
agent_role: "checkout"
domain: "ecommerce"
---

## When to use
Use this skill for standard ecommerce tasks where the agent performs the role of **checkout**.

## Discovery guidance
This skill provides broad ecommerce support and is suitable for routine requests.
It is not specialized for any single constraint pattern.

## Workflow
1. Read the task and identify the requested output.
2. Extract general constraints and key entities.
3. Produce a simple recommendation for the checkout subtask.
4. Return a concise handoff-friendly summary.

## Good patterns
- routine subtasks
- simple filtering support
- handoff-friendly summaries

## Examples
- A standard ecommerce request involving checkout
- A routine task with a few simple constraints
- A request needing a short structured response
