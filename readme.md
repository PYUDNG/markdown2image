# markdown2image.py

Python utility to convert markdown and html to image using [markdown](https://github.com/Python-Markdown/markdown) and [playwright](https://github.com/microsoft/playwright).

## Installing
1. Clone the repo or download zip, then copy markdown2image.py to your project folder
2. `pip install -r requirements.txt`
3. `playwright install chromium`

## Usage

``` python
from markdown2image import html2image, markdown2image

html2image(html_code, save_path)
markdown2image(markdown_code, save_path)
```

for code example, see main.py.