import os
from PIL import Image

for file in os.listdir('images/fulls'):
    image = Image.open('images/fulls/' + file)
    image.thumbnail((512,512), Image.ANTIALIAS)
    image.save('images/thumbs/' + file, "JPEG")
