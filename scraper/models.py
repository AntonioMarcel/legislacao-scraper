from dataclasses import dataclass
from typing import Optional

@dataclass
class Legislacao:
    titulo: str
    ementa: str
    status: Optional[str] = None
    link_ficha: Optional[str] = None
    link_norma: Optional[str] = None

