from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Evaluacion:
    nombre: str
    resolucion: str
    calificacion: dict | None = None
    comentarios: str | None = None
    tarea: str | None = None
