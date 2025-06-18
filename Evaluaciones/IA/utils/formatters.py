from __future__ import annotations

import json
from typing import Any


def to_pretty_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)
