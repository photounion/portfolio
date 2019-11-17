import os
from PIL import Image

for dir in os.listdir():
    if os.path.exists(dir + '/images') and (not os.path.exists(dir + '/images/thumbs') or len(os.listdir(dir + '/images/thumbs')) == 0):
        if not os.path.exists(dir + '/images/thumbs'):
            os.mkdir(dir + '/images/thumbs')
        for file in os.listdir(dir + '/images/fulls'):
            image = Image.open(dir + '/images/fulls/' + file)
            image.thumbnail((512,512), Image.ANTIALIAS)
            image.save(dir + '/images/thumbs/' + file, "JPEG")

print('Done!')
