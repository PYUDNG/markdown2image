import time, os
print(f'Program started at {time.time()}')

from markdown2image import sync_api as md2img

print(f'Browser context ready at {time.time()}')
os.chdir('./tests')
for filename in os.listdir('./html'):
    md2img.html2image(open(f'./html/{filename}', 'r', encoding='utf-8').read(), f'./output/html2image/{os.path.splitext(filename)[0]}.png')
    print(f'HTML screenshoted at {time.time()}')

print(f'HTML screenshot finish at {time.time()}')
for filename in os.listdir('./markdown'):
    md2img.markdown2image(open(f'./markdown/{filename}', 'r', encoding='utf-8').read(), f'./output/markdown2image/{os.path.splitext(filename)[0]}.png')
    print(f'Markdown screenshoted at {time.time()}')