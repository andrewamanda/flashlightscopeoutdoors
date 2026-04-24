from ecomstore.settings import MEDIA_ROOT

from random import choice
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import hashlib
import time


SECRET_KEY = 'tec@!@q*_wq8er3#f2xe)209xnyuv@=ls8bepv!$qz=z*6vo31'
SALT = SECRET_KEY[:20]


def createCaptcha(request):

    # PIL elements, sha for hash


    # create a 5 char random strin and sha hash it, note that there is no big i

    lenCaptchar = ''.join([choice('567') for i in range(1)])
    imgtext = ''.join([choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789') for i in range(int(lenCaptchar))])

    temp = MEDIA_ROOT + "/images/" + str(request.META.get('HTTP_X_FORWARDED_FOR')) + imgtext + '.jpg'
    temppath = "/static/images/" + str(request.META.get('HTTP_X_FORWARDED_FOR')) + imgtext + '.jpg'

    hash = hashlib.sha512()
    txt = SALT+imgtext
    hash.update(txt.encode('utf-8'))
    imghash = hash.hexdigest()
        # create an image with the string (media is the folder with static files accessed by /site_media)
        # PIL "code" - open image, add text using font, save as new
    im=Image.open(MEDIA_ROOT+'/images/siteImg/bg.jpg')
    draw=ImageDraw.Draw(im)
    font=ImageFont.truetype(MEDIA_ROOT+'/images/siteImg/verdana.ttf', 24)
    draw.text((10,10),imgtext, font=font, fill=(100,100,50))


        # save as a temporary image
        # I use user IP for the filename, SITE_IMAGES_DIR_PATH - system path to folder for images
    im.save(temp, "JPEG")
    return {
        'imgpath': temppath,
        'imghash': imghash
    }

def verifyCaptcha(imghash, imgtext):
    #print imghash
    #print hashlib.sha1.new(SALT+imgtext).hexdigest()

    hash = hashlib.sha512()
    txt = SALT+imgtext
    hash.update(txt.encode('utf-8'))
    imghash0 = hash.hexdigest()
    if imghash == imghash0:
        return True
    else:
        return False
