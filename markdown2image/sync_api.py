from playwright.sync_api import sync_playwright, Playwright
import markdown
import json

# Init browser and context
_playwright: Playwright = sync_playwright().start()
_browser = _playwright.chromium.launch()
_context = _browser.new_context()

def html2image(html: str, path: str):
    with _context.new_page() as page:
        page.evaluate(f'() => document.write({json.dumps(html)})')
        page.screenshot(path=path, full_page=True)

def markdown2image(md: str, path: str):
    html = markdown.markdown(md)
    html2image(html, path)