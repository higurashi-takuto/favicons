import os
import glob

from PIL import Image

paths = glob.glob('*/favicon.png')

for path in paths:
    img = Image.open(path)
    dirname = os.path.dirname(path)
    output_path = f'{dirname}/favicon.ico'
    img.save(output_path)
