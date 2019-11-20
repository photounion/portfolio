import os
from PIL import Image

for dir in os.listdir():
    if os.path.exists(dir + '/images'):
        for file in os.listdir(dir):
            if (file[-4:] == '.jpg' or file[-4:] == '.png') and not os.path.exists(dir + '/' + dir + '_full/' + file):
                #print('ok')
                #try:
                #    os.rename(dir + '/' + dir + '_thumb', dir + '/' + dir + '_full')
                #except:
                #    pass
                os.mkdir(dir + '/' + dir + '_full')
                print(dir + '/' + file + ' renamed to ' + dir + '_full/' + dir + '/' + file)
                os.rename(dir + '/' + file, dir + '/' + dir + '_full/' + file)
                image = Image.open(dir + '/' + dir + '_full/' + file)
                image.thumbnail((512,512), Image.ANTIALIAS)
                image.save(dir + '/' + file, "JPEG")

print('Done!')
