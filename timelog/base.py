
import os.path
import shutil

import qrcode
from qrcode.image.pure import PymagingImage
import qrtools
import requests

# TODO: Accept image
def read_record(image_url):
    """ Reads a qr code image and returns the data if possible """
    qr = qrtools.QR()
    r = requests.get(image_url, stream=True)
    if r.status_code == 200:
        with open('qr.png', 'wb') as image_file:
            for chunk in r.iter_content(1024):
                image_file.write(chunk)
        with open('qr.png', 'rb') as image_file:
            try:
                qr.decode(image_file)
            except Exception, e:
                raise Exception('Can\'t decode image: ' + str(e))
            return qr.data
    raise Exception('No image fetched.')

read_record(image_url='http://i.imgur.com/fers0Gj.png')