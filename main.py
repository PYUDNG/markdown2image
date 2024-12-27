import time, os
print(f'Program started at {time.time()}')

from html2image import html2image, markdown2image

print(f'Browser context ready at {time.time()}')
for filename in os.listdir('./html'):
    html2image(open(f'./html/{filename}', 'r', encoding='utf-8').read(), f'./output/html2image/{os.path.splitext(filename)[0]}.png')
    print(f'HTML screenshoted at {time.time()}')

print(f'HTML screenshot finish at {time.time()}')
for filename in os.listdir('./markdown'):
    markdown2image(open(f'./markdown/{filename}', 'r', encoding='utf-8').read(), f'./output/markdown2image/{os.path.splitext(filename)[0]}.png')
    print(f'Markdown screenshoted at {time.time()}')