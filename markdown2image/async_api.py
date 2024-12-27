from playwright.async_api import async_playwright, Playwright, Browser, BrowserContext
import markdown
import json

# Init browser and context
_playwright: Playwright
_browser: Browser
_context: BrowserContext
initialized: bool = False

async def _init():
    global _playwright, _browser, _context
    _playwright = await async_playwright().start()
    _browser = await _playwright.chromium.launch()
    _context = await _browser.new_context()

async def html2image(html: str, path: str):
    if not initialized: await _init()
    
    page = await _context.new_page()
    await page.evaluate(f'() => document.write({json.dumps(html)})')
    await page.screenshot(path=path, full_page=True)

async def markdown2image(md: str, path: str):
    html = markdown.markdown(md)
    await html2image(html, path)