from playwright.async_api import Page
from .config import SELECTORS
from .models import Legislacao

class Parser:
    async def parse(self, page: Page) -> list[Legislacao]:
        cards = page.locator(SELECTORS["cards"])
        legislacao_data = []

        for card in await cards.all():

            titulo = await card.locator(SELECTORS["titulo"]).inner_text()
            titulo = titulo.replace("Veto Parcial", "").strip()
            status = await card.locator(SELECTORS["status"]).inner_text()
            ementa = await card.locator(SELECTORS["ementa"]).inner_text()
            ementa = ementa.replace("Vigência", "").strip()
            botoes = card.locator(SELECTORS["botoes"])

            link_ficha = None
            link_norma = None

            for botao in await botoes.all():
                texto = await botao.inner_text()
                href = await botao.get_attribute("href")

                if "Ficha" in texto:
                    link_ficha = href
                elif "Integral" in texto:
                    link_norma = href

            legislacao_obj = Legislacao(
                titulo=titulo,
                status=status,
                ementa=ementa,
                link_ficha=link_ficha,
                link_norma=link_norma,

            )
            legislacao_data.append(legislacao_obj)

        print(legislacao_data)
