from typing import Optional
from playwright.sync_api import sync_playwright, Playwright
import markdown
import json

# Init browser and context
_playwright: Playwright = sync_playwright().start()
_browser = _playwright.chromium.launch()
_context = _browser.new_context(viewport={'width': 800, 'height': 1})

def html2image(html: str, path: str, *, width: Optional[int] = None):
    with _context.new_page() as page:
        if width != None: page.set_viewport_size({"width": width, "height": 1})
        page.evaluate(f'() => document.write({json.dumps(html)})')
        page.screenshot(path=path, full_page=True)

def markdown2image(md: str, path: str, width: Optional[int] = None):
    html = markdown.markdown(md)
    html2image(html, path, width=width)