from __future__ import annotations


def is_valid_json(data: str) -> bool:
    import json
    try:
        json.loads(data)
        return True
    except Exception:
        return False
