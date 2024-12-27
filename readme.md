# markdown2image.py

[![Hippocratic License HL3-FULL](https://img.shields.io/static/v1?label=Hippocratic%20License&message=HL3-FULL&labelColor=5e2751&color=bc8c3d)](https://firstdonoharm.dev/version/3/0/full.html)

Python utility to convert markdown and html to image using [markdown](https://github.com/Python-Markdown/markdown) and [playwright](https://github.com/microsoft/playwright).

## Installing
``` bash
pip install markdown2image
playwright install chromium
```

## Usage
Just 
``` python
from markdown2image import sync_api as md2img

md2img.html2image(html_code, save_path)
md2img.html2image(html_code, save_path, width=1080)
md2img.markdown2image(markdown_code, save_path)
md2img.markdown2image(markdown_code, save_path, width=1080)
```

Or in a running event loop,

``` python
from markdown2image import async_api as md2img

async def func():
    await md2img.html2image(html_code, save_path)
    await md2img.html2image(html_code, save_path, width=1080)
    await md2img.markdown2image(markdown_code, save_path)
    await md2img.markdown2image(markdown_code, save_path, width=1080)
```

See main.py for example code