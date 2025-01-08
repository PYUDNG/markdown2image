from typing import Optional
from playwright.async_api import async_playwright, Playwright, Browser, BrowserContext, Page
import markdown

# Init browser and context
_playwright: Playwright
_browser: Browser
_context: BrowserContext
_page: Page
initialized: bool = False

async def _init():
    global _playwright, _browser, _context
    _playwright = await async_playwright().start()
    _browser = await _playwright.chromium.launch()
    _context = await _browser.new_context(viewport={'width': 800, 'height': 1})
    _page = _context.new_page()

async def html2image(html: str, path: str, *, width: Optional[int] = None):
    if not initialized: await _init()
    
    await _page.reload(wait_until='commit')
    if width != None: await _page.set_viewport_size({"width": width, "height": 1})
    await _page.set_content(html=html, wait_until='load')
    await _page.screenshot(path=path, full_page=True)

async def markdown2image(md: str, path: str, width: Optional[int] = None):
    html = markdown.markdown(md)
    await html2image(html, path, width=width)