import asyncio
from playwright.async_api import async_playwright
from scraper import Legislacao, JsonlWriter, Parser, SELECTORS

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://legislacao.presidencia.gov.br/#")
        await page.locator("a.nav-link.dropdown-toggle.pl-4.pr-4.mr-2.btn.btn-secondary.btn-round.text-white.d-none.d-sm-block").click()
        await page.wait_for_selector(SELECTORS["cards"])

        p = Parser()
        await p.parse(page)
        input("Enter para fechar o navegador")
        await browser.close()

asyncio.run(main())

