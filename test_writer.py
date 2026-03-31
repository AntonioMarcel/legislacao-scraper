from models import Legislacao
from writer import JsonlWriter

leg1 = Legislacao(
    titulo="Decreto nº 12.911",
    ementa="Declara de interesse social para fins de desapropriação",
    link_norma="https://www.planalto.gov.br/...",
    link_ficha="https://legislacao.presidencia.gov.br/..."
)

leg2 = Legislacao(
    titulo="Medida Provisória nº 1.347",
    ementa="Abre crédito extraordinário no valor de R$ 285.000.000,00",
    link_norma=None,
    link_ficha=None
)

with JsonlWriter("test_output.jsonl") as writer:
    writer.write(leg1)
    writer.write(leg2)

print("Feito! Abre o test_output.jsonl e confere.")