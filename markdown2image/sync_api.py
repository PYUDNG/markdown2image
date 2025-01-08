from typing import Optional
from playwright.sync_api import sync_playwright, Playwright
import markdown

# Init browser and context
_playwright: Playwright = sync_playwright().start()
_browser = _playwright.chromium.launch()
_context = _browser.new_context(viewport={'width': 800, 'height': 1})
_page = _context.new_page()

def html2image(html: str, path: str, *, width: Optional[int] = None):
    _page.reload(wait_until='commit')
    if width != None: _page.set_viewport_size({"width": width, "height": 1})
    _page.set_content(html=html, wait_until='load')
    _page.screenshot(path=path, full_page=True)

def markdown2image(md: str, path: str, width: Optional[int] = None):
    html = markdown.markdown(md)
    html2image(html, path, width=width)