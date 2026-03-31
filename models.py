from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class Legislacao:
    titulo: str
    ementa: str
    link_norma: Optional[str] = None
    link_ficha: Optional[str] = None

