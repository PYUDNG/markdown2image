from typing import Optional, TypedDict
from playwright.async_api import async_playwright, Playwright, Browser, BrowserContext, Page
import markdown

# Init browser and context
class T_status_page(TypedDict):
    id: int
    busy: bool
    page: Page

_playwright: Playwright
_browser: Browser
_context: BrowserContext
_pages: list[T_status_page]
initialized: bool = False

async def new_page() -> T_status_page:
    global _pages
    page = await _context.new_page()
    status_page: T_status_page = {
        'id': len(_pages),
        'busy': False,
        'page': page
    }
    _pages.append(status_page)
    return status_page

async def get_idle_page() -> T_status_page:
    global _pages
    for status_page in _pages:
        if not status_page['busy']:
            return status_page
    status_page = await new_page()
    return status_page

def set_page_status(page_id: int, status: bool):
    global _pages
    for status_page in _pages:
        if status_page['id'] == page_id:
            status_page['busy'] = status
            return
    raise Exception(f'No page found with provided page_id {repr(page_id)}')

async def _init():
    global _playwright, _browser, _context, _pages, initialized
    _playwright = await async_playwright().start()
    _browser = await _playwright.chromium.launch()
    _context = await _browser.new_context(viewport={'width': 800, 'height': 1})
    _pages = []
    initialized = True

async def html2image(html: str, path: str, *, width: Optional[int] = None):
    if not initialized: await _init()
    
    # Get an idle page to render
    status_page = await get_idle_page()
    set_page_status(status_page['id'], True)
    page = status_page['page']
    
    # render & screenshot
    await page.reload(wait_until='commit')
    if width != None: await page.set_viewport_size({"width": width, "height": 1})
    await page.set_content(html=html, wait_until='load')
    await page.screenshot(path=path, full_page=True)
    
    # release page to idle pages
    set_page_status(status_page['id'], False)

async def markdown2image(md: str, path: str, width: Optional[int] = None):
    html = markdown.markdown(md)
    await html2image(html, path, width=width)