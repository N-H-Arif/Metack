# src/client/agents/http_agent_robust.py
from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple
import requests


class HTTPAgentRobust:
    """
    Robust chat-completions client for OpenAI-compatible servers.

    Works with:
      - vLLM OpenAI server
      - llama.cpp OpenAI-compatible server (GGUF), which often uses timings.predicted_n

    Key behavior:
      - Sends both max_tokens (OpenAI) and n_predict (llama.cpp).
      - Returns assistant text even if response schema varies.
      - Can optionally return raw response JSON for debugging.
    """

    def __init__(
        self,
        url: str,
        model: str,
        temperature: float = 0.0,
        max_tokens: int = 256,
        timeout: int = 600,
        headers: Optional[Dict[str, str]] = None,
        extra_body: Optional[Dict[str, Any]] = None,
    ):
        self.url = url
        self.model = model
        self.temperature = temperature
        self.max_tokens = int(max_tokens)
        self.timeout = timeout
        self.headers = headers or {"Content-Type": "application/json"}
        self.extra_body = extra_body or {}

    @staticmethod
    def _extract_text(resp: Dict[str, Any]) -> str:
        # Standard OpenAI chat.completions: choices[0].message.content
        try:
            c = resp["choices"][0]["message"]["content"]
            if isinstance(c, str):
                return c
        except Exception:
            pass

        # Some servers: choices[0].text
        try:
            t = resp["choices"][0]["text"]
            if isinstance(t, str):
                return t
        except Exception:
            pass

        # Content as parts: [{"type":"text","text":"..."}]
        try:
            c = resp["choices"][0]["message"]["content"]
            if isinstance(c, list):
                for part in c:
                    if isinstance(part, dict) and isinstance(part.get("text", None), str):
                        return part["text"]
        except Exception:
            pass

        return ""

    def inference_with_debug(
        self,
        messages: List[Dict[str, str]],
    ) -> Tuple[str, Dict[str, Any], Dict[str, Any]]:
        """
        Returns:
          assistant_text, raw_response_json, request_payload
        """
        body: Dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "temperature": float(self.temperature),

            # OpenAI / vLLM style
            "max_tokens": self.max_tokens,

            # llama.cpp OpenAI server style
            "n_predict": self.max_tokens,

            "stream": False,
        }
        body.update(self.extra_body)

        r = requests.post(self.url, headers=self.headers, json=body, timeout=self.timeout)
        r.raise_for_status()
        data = r.json()
        text = self._extract_text(data)
        return text, data, body

    def inference(self, messages: List[Dict[str, str]]) -> str:
        text, _, _ = self.inference_with_debug(messages)
        return text
