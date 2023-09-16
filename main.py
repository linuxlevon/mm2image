from html2image import Html2Image

# from pathlib import Path
#
#
# for i in range(1, 11):
#     Path(f'./file{i}.txt').touch()
#
#
#

hti = Html2Image()
hti.screenshot(url='https://www.python.org', save_as='python.png')