# Selection-Optimized Metadata for Agent and Skill Routing in Multi-Agent LLM Systems

This repository contains NeurIPS submission code for Selection-Optimized Metadata for Agent and Skill Routing in Multi-Agent LLM Systems. The artifact evaluates how attacker-controlled developers can manipulate published metadata, such as `AgentCard` and `SkillCard` descriptions, tags, and discovery text, to increase the likelihood that their agents or skills are selected by an LLM router.


The project extends AgentBench-style routing with multi-agent registries, generated agent/skill metadata, prompt-level and system-level defenses, and evaluation scripts for horizontal, vertical, and hybrid multi-agent architectures.

## Overview

Modern multi-agent systems often choose remote agents or skills based on lightweight published metadata rather than verified capabilities. This repository studies that routing surface.

We simulate a client/router agent that receives a user task and selects one candidate from a metadata registry. One developer, `devB`, is treated as attacker-controlled. The attacker modifies only metadata while preserving the candidate role and identity.

The artifact supports two metadata levels:

1. **AgentCard attacks**: manipulation of agent name, description, and tags.
2. **SkillCard attacks**: manipulation of `SKILL.md` frontmatter and discovery-oriented skill text.

The artifact evaluates three multi-agent routing architectures:

- **Horizontal**: same-level agent selection with a second handoff-style routing step.
- **Vertical**: staged routing across step-1 and step-2 candidate pools.
- **Hybrid**: three-step chained routing across multiple role-specific pools.

## Metrics

Each run reports:

- `T1R`: first-step attacker routing rate.
- `Selection`: final attacker selection rate.
- `CAR`: cross-agent capture rate, measuring whether attacker selection propagates across routing steps.

Clean and attacked conditions use the same tasks, model, seed, candidate count, and metadata budget.

## Repository Structure

- `scripts/run_all_arch.py` - main AgentCard experiment runner for local OpenAI-compatible endpoints.
- `scripts/run_all_arch_closed.py` - AgentCard runner for OpenAI-compatible closed-model APIs.
- `scripts/run_all_skillbench_arch.py` - main SkillCard experiment runner.
- `scripts/card_pipeline.py` - metadata normalization, hard-negative decoys, and attack-strength controls.
- `scripts/defenses.py` - prompt-level defenses such as delimiters, instructional warnings, paraphrasing, rewriting, etc.
- `scripts/gen_15_scenarios.py` - generates the 15 AgentCard benchmark scenarios.
- `scripts/gen_skillbench_scenarios.py` - generates SkillCard packages for the same scenarios.
- `scripts/skillbench_io.py` - parser and serializer utilities for generated `SKILL.md` packages.
- `scripts/run_all_arch_agrail.py` - optional AGrail guardrail integration.
- `scenarios/` - generated tasks, clean metadata, attacked metadata, and skill packages.
- `configs/` - configuration files.


## Installation

Create a Python environment:

```bash
conda create -n agent-bench python=3.9 -y
conda activate agent-bench
pip install -U pip
pip install -r requirements.txt
```

On Windows CMD, run experiments from the repository root and expose the package path:

```cmd
conda activate agent-bench
set PYTHONPATH=%CD%
```

## Local Model Setup

The local experiments assume an OpenAI-compatible chat-completion endpoint at:

```text
http://localhost:8000/v1/chat/completions
```

One tested setup uses `llama.cpp` from WSL. Example model downloads:

```bash
hf download bartowski/Qwen2.5-3B-GGUF Qwen2.5-3B-Q4_K_M.gguf --local-dir ~/llama.cpp/models
hf download bartowski/gemma-2-2b-it-GGUF gemma-2-2b-it-Q4_K_M.gguf --local-dir ~/llama.cpp/models
hf download bartowski/Llama-3.2-3B-Instruct-GGUF Llama-3.2-3B-Instruct-Q4_K_M.gguf --local-dir ~/llama.cpp/models
```

Start a local server, for example:

```bash
~/llama.cpp/build-cuda/bin/llama-server \
  -m ~/llama.cpp/models/Qwen2.5-3B-Q4_K_M.gguf \
  --host 0.0.0.0 \
  --port 8000 \
  -ngl 35
```

Other evaluated local model tags include `gemma2b`, `llama3b`, `qwen32b`, and `gemma40b`, depending on the GGUF file served by `llama-server`.

## Quickstart: AgentCard Experiment

Run one small local AgentCard experiment:

```cmd
set PYTHONPATH=%CD%
python scripts/run_all_arch.py ^
  --url http://localhost:8000/v1/chat/completions ^
  --model Qwen2.5-3B-Q4_K_M.gguf ^
  --model_tag qwen3b ^
  --scenario travel_trip ^
  --defense none ^
  --seed 0 --num_seeds 1 ^
  --attack_strength_p 0.9
```

This evaluates clean and attacked AgentCards on the `travel_trip` scenario across horizontal, vertical, and hybrid routing.

Outputs are written to:

```text
outputs/agentcard_attack/qwen3b/travel_trip/def_none/seed_0/
```

## Quickstart: SkillCard Experiment

Run one local SkillCard experiment:

```cmd
set PYTHONPATH=%CD%
python scripts/run_all_skillbench_arch.py ^
  --url http://localhost:8000/v1/chat/completions ^
  --model Qwen2.5-3B-Q4_K_M.gguf ^
  --model_tag qwen3b ^
  --scenario travel_trip ^
  --defense none ^
  --seed 0 --num_seeds 1
```

Outputs are written to:

```text
outputs/skillbench_attack/qwen3b/travel_trip/def_none/seed_0/
```

## Closed-Model Runs

Closed-model runs use `scripts/run_all_arch_closed.py`. Set the API key through the environment; do not place keys in commands, scripts, notebooks, or committed files.

```cmd
set OPENAI_API_KEY=<your_api_key>
set PYTHONPATH=%CD%
python scripts/run_all_arch_closed.py ^
  --url https://api.openai.com/v1/chat/completions ^
  --model gpt-5-mini ^
  --model_tag gpt5mini ^
  --scenario travel_trip ^
  --defense none ^
  --seed 0 --num_seeds 1 ^
  --attack_strength_p 0.9
```

## Defenses

The `--defense` flag controls prompt-level defenses, for example:

```cmd
python scripts/run_all_arch.py --model Qwen2.5-3B-Q4_K_M.gguf --model_tag qwen3b --scenario travel_trip --defense delimiters
```

Common defense options:

- `none`
- `delimiters`
- `instructional`
- `rewrite`
- `paraphrase`


The AGrail integration is optional and requires a separate AGrail checkout:

```cmd
set OPENAI_API_KEY=<your_api_key>
set PYTHONPATH=%CD%
python scripts/run_all_arch_agrail.py ^
  --url http://localhost:8000/v1/chat/completions ^
  --model Qwen2.5-3B-Q4_K_M.gguf ^
  --model_tag agrail_test ^
  --scenario travel_trip ^
  --defense agrail4agent ^
  --agrail_root ..\AGrail4Agent-main ^
  --agrail_model gpt-5-mini ^
  --seed 0 --num_seeds 1 ^
  --attack_strength_p 0.9
```

## Optimizers

The repository also includes black-box metadata optimizers:

```cmd
set PYTHONPATH=%CD%
python scripts/auto_optimize_agentcard.py ^
  --url http://localhost:8000/v1/chat/completions ^
  --model Qwen2.5-3B-Q4_K_M.gguf ^
  --scenario travel_trip ^
  --defense none ^
  --objective Selection ^
  --iters 20 ^
  --task_cap 20 ^
  --seed 0
```

SkillCard optimization is available through:

```cmd
set PYTHONPATH=%CD%
python scripts/auto_optimize_skillbench.py ^
  --url http://localhost:8000/v1/chat/completions ^
  --model Qwen2.5-3B-Q4_K_M.gguf ^
  --scenario travel_trip ^
  --objective Selection ^
  --seed 0
```

## Reproducibility Notes

Default main-run settings:

| Setting | Default / Typical Value |
|---|---:|
| Scenario task count | 80 tasks per scenario |
| Default seed | 0 |
| Temperature | 0.0 |
| Max output tokens | 256, or 128 for some larger local models |
| Beam size | effectively 1 |
| Attacker developer prefix | `devB.` |
| AgentCard max description words | 12 |
| Matched decoys per step | 2 |
| Typical attack strength | 0.9 |

Each seed writes a separate `seed_<id>` folder. Per-task traces are stored as JSONL files, and aggregate metrics are stored as JSON files.

## Sensitive Content Removal

This artifact is intended for reproducible security research on metadata-driven selection behavior. The repository should not include generated results, model weights, local caches, or credentials.

No production credentials or private user data are required for the artifact. API keys, if used for closed-model or AGrail experiments, must be supplied through environment variables and must not be committed.
