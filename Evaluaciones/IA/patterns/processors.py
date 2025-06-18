from __future__ import annotations

"""Generic data processing helpers."""

from typing import List, Dict, Any


def filter_no_realiza(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [item for item in items if item.get("resolucion", "").strip().lower() != "no realiza"]
