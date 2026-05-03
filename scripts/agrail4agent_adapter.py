import os
import sys
from pathlib import Path
from typing import Any, Dict, Tuple


def _ensure_agrail_importable(agrail_root: str) -> Path:
    root = Path(agrail_root).resolve()
    if not root.exists():
        raise FileNotFoundError(f"AGrail root not found: {root}")

    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    return root


def agrail_guardrail_check(
    *,
    agrail_root: str,
    agrail_model: str = "gpt-5-mini",
    agent_model: str = "",     # <-- ADD THIS
    user_information: str = "",
    agent_action: str = "",
    tools: str = "",
    environment_text: str = "",
    user_request: str = "",
    output: str = "",
    agent_output: str = "",
    retrieve_file: str = "",
    memory_file: str = "",
    update_memory: str = "",
):
    ...
    """
    AGrail wrapper for AgentBench.

    - Accepts multiple kwarg aliases to match run_all_arch_agrail.py
    - Fails closed (unsafe) if AGrail crashes
    - Does NOT modify AGrail source code
    """

    # -----------------------------
    # Alias resolution (critical)
    # -----------------------------
    if not user_information and user_request:
        user_information = user_request

    if not agent_action:
        if output:
            agent_action = output
        elif agent_output:
            agent_action = agent_output

    if not tools and environment_text:
        tools = environment_text

    meta: Dict[str, Any] = {
        "agrail_model": agrail_model,
        "agrail_root": str(Path(agrail_root).resolve()),
        "ran": False,
        "error": None,
    }

    # -----------------------------
    # Make AGrail importable
    # -----------------------------
    _ensure_agrail_importable(agrail_root)

    # -----------------------------
    # Ensure API key visible to:
    # - OpenAI SDK
    # - LangChain OpenAIEmbeddings
    # -----------------------------
    key = os.environ.get("OPENAI_API_KEY", "")
    if not key:
        raise RuntimeError("OPENAI_API_KEY is not set. AGrail requires it.")

    os.environ["OPENAI_API_KEY"] = key
    os.environ.setdefault("OPENAI_API_BASE", "https://api.openai.com/v1")

    try:
        from DAS.guardrail import guard_rail  # AGrail import

        meta["ran"] = True

        # -----------------------------
        # Call AGrail guardrail
        # -----------------------------
        is_safe, check_process, tool_process, length = guard_rail(
            user_information=user_information,
            agent_action=agent_action,
            tools=tools,
            model=agrail_model,
        )

        meta.update(
            {
                "is_safe": bool(is_safe),
                "check_process": check_process,
                "tool_process": tool_process,
                "length": length,
            }
        )

        return bool(is_safe), meta

    except IndexError as e:
        # AGrail JSON extraction failure (common)
        meta["error"] = {
            "type": "IndexError",
            "msg": str(e),
            "note": "AGrail JSON extraction failed — marked unsafe (fail-closed).",
        }
        return False, meta

    except Exception as e:
        # Any other AGrail internal error
        meta["error"] = {
            "type": type(e).__name__,
            "msg": str(e),
        }
        return False, meta