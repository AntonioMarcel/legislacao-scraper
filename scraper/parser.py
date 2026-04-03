from playwright.async_api import Page
from .config import SELECTORS
from .models import Legislacao

class Parser:
    async def parse(self, page: Page) -> list[Legislacao]:
        cards = page.locator(SELECTORS["cards"])
        legislacao_data = []

        for card in await cards.all():
            titulo = await card.locator(SELECTORS["titulo"]).inner_text()
            status = await card.locator(SELECTORS["status"]).inner_text()
            ementa = await card.locator(SELECTORS["ementa"]).inner_text()
            ementa = ementa.replace("Vigência", "").strip()
            botoes = card.locator(SELECTORS["botoes"])

            link_list = []
            for botao in await botoes.all():
                href = await botao.get_attribute("href")
                link_list.append(href)

            legislacao_obj = Legislacao(
                titulo=titulo,
                status=status,
                ementa=ementa,
                link_ficha=link_list[0],
                link_norma=link_list[1],

            )
            legislacao_data.append(legislacao_obj)

        print(legislacao_data)
