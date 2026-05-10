from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class Gasto:
    descricao: str
    valor: float
    categoria: str
    data: str = field(default_factory=lambda: datetime.now().strftime("%d/%m/%Y %H:%M"))

    def __str__(self):
        return f"{self.data} | {self.categoria.upper()} | {self.descricao}: R$ {self.valor:.2f}"