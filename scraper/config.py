"""
Seletores CSS utilizados no scraper.

Referência de sintaxe:
    "."  indica classes
    ">"  indica filho direto
    " "  indica qualquer descendente
    "+"  indica elemento seguinte na mesma hierarquia (apenas o próximo irmão imediato)
    "~"  indica todos os irmãos seguintes na mesma hierarquia
"""

BASE_URL = "https://legislacao.presidencia.gov.br/#"

SELECTORS = {
    "btn_pesquisar": "a.btn.btn-secondary.btn-round",
    "total_resultados": "h4.pb-2.fw-bold",
    "cards": "div.card.p-2.pr-3.pl-3.w-100",
    "titulo": "h4.card-title",
    "status": "p.card-category",
    "ementa": "p.pt-2",
    "ementa_fallback": "p.pt-2 + :is(p, div)", 
    "botoes": "ul.list-inline li a.btn",
}
