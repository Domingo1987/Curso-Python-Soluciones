from __future__ import annotations

import os
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class Settings:
    api_key: str
    assistant_id: str | None = None


def load_settings() -> Settings:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    assistant_id = os.getenv("OPENAI_ASSISTANT_ID")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found")
    return Settings(api_key=api_key, assistant_id=assistant_id)
