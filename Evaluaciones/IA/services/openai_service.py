from __future__ import annotations

import os
from dotenv import load_dotenv
from openai import OpenAI


class OpenAIService:
    """Simple wrapper to load credentials and provide an OpenAI client."""

    def __init__(self) -> None:
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment")
        self.client = OpenAI(api_key=api_key)

    def get_client(self) -> OpenAI:
        return self.client
