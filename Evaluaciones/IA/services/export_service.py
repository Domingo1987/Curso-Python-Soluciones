from __future__ import annotations

import pandas as pd
from typing import Any, List


def json_to_csv(data: List[dict[str, Any]], csv_path: str) -> None:
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)
