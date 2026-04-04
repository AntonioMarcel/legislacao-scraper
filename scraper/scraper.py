import asyncio
import math

from playwright.async_api import async_playwright

from .config import BASE_URL, SELECTORS
from .parser import Parser
from .writer import JsonlWriter

class Scraper:
    def __init__(self, output_path="output/output.jsonl"):
        self.parser = Parser()
        self.writer = JsonlWriter(output_path)

    async def run(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={"width": 1280, "height": 900},
                user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = await context.new_page()

            await page.goto(BASE_URL)
            await page.evaluate("pesquisaLegislacao('0')")
            await page.wait_for_selector(SELECTORS["cards"])

            await page.wait_for_selector(SELECTORS["total_resultados"])
            total_resultados = await page.locator(SELECTORS["total_resultados"]).inner_text()
            total_resultados = int(total_resultados.replace("resultados encontrados", "").replace(".", "").strip())
            total_paginas = math.ceil(total_resultados / 10)
            print(total_paginas)

            with self.writer as writer:

                for pagina in range(total_paginas):
                    print(f"Página {pagina+1} de {total_paginas}")
                    offset = pagina * 10
                    await page.evaluate(f"pesquisaLegislacao('{pagina}', '{offset}')")
                    await page.wait_for_selector(SELECTORS["cards"])
                    legislacao_data = await self.parser.parse(page) # legislacao_data == lista de objs Legislacao

                    for legislacao_obj in legislacao_data:
                        writer.write(legislacao_obj)

            await browser.close()
