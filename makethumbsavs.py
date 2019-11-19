import os
from PIL import Image

for dir in os.listdir():
    if os.path.exists(dir + '/images'):
        for file in os.listdir(dir):
            if (file[-4:] == '.jpg' or file[-4:] == '.png') and file.find('thumb') == -1:
                print('ok')
                try:
                    os.rename(dir + '/' + dir, dir + '/' + dir + '_thumb')
                except:
                    pass
                #print(dir + '/' + file + ' renamed to ' + dir + '/' + dir + '/' + file)
                #os.rename(dir + '/' + file, dir + '/' + dir + '/' + file)
                #print(dir + '/' + file[:-4] + '_thumb' + file[-4:] + ' renamed to ' + dir + '/' + file)
                #os.rename(dir + '/' + file[:-4] + '_thumb' + file[-4:], dir + '/' + file)
                #image = Image.open(dir + '/' + file)
                #image.thumbnail((512,512), Image.ANTIALIAS)
                #image.save(dir + '/' + file[:-4] + '_thumb' + file[-4:], "JPEG")

print('Done!')
