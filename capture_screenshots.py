"""
Script para capturar screenshots de todas as páginas do zavvy.com.br
"""
import asyncio
import os
from playwright.async_api import async_playwright

BASE_URL = "https://zavvy.com.br"
OUTPUT_DIR = "screenshots"

PAGES = [
    {
        "folder": "home",
        "url": "https://zavvy.com.br/",
        "sections": [
            {"name": "01-hero", "scroll": 0},
            {"name": "02-whatsapp-demo", "anchor": "#whatsapp-demo"},
            {"name": "03-como-funciona", "anchor": "#como-funciona"},
            {"name": "04-funcionalidades", "anchor": "#funcionalidades"},
            {"name": "05-preco", "anchor": "#preco"},
            {"name": "06-faq", "anchor": "#faq"},
            {"name": "07-footer", "scroll": 99999},
        ],
    },
    {
        "folder": "termos-de-uso",
        "url": "https://zavvy.com.br/termos-de-uso",
        "sections": None,  # full page
    },
    {
        "folder": "politica-de-privacidade",
        "url": "https://zavvy.com.br/politica-de-privacidade",
        "sections": None,  # full page
    },
]


async def capture_page(page, config):
    folder = os.path.join(OUTPUT_DIR, config["folder"])
    os.makedirs(folder, exist_ok=True)

    await page.goto(config["url"], wait_until="networkidle")
    await page.wait_for_timeout(1500)

    if config["sections"] is None:
        # Full page screenshot
        path = os.path.join(folder, "full-page.png")
        await page.screenshot(path=path, full_page=True)
        print(f"  Saved: {path}")
    else:
        for section in config["sections"]:
            if "anchor" in section:
                await page.evaluate(f"""
                    const el = document.querySelector('{section["anchor"]}');
                    if (el) el.scrollIntoView({{behavior: 'instant', block: 'start'}});
                """)
            elif "scroll" in section:
                await page.evaluate(f"window.scrollTo(0, {section['scroll']})")

            await page.wait_for_timeout(800)

            path = os.path.join(folder, f"{section['name']}.png")
            await page.screenshot(path=path)
            print(f"  Saved: {path}")


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 900},
            locale="pt-BR",
        )
        page = await context.new_page()

        for config in PAGES:
            print(f"\n[{config['folder']}] {config['url']}")
            await capture_page(page, config)

        await browser.close()
        print("\nCaptura concluída!")


if __name__ == "__main__":
    asyncio.run(main())
