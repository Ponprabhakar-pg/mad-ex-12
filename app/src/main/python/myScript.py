from PIL import Image
import cv2
import base64
from os.path import dirname, join
from com.chaquo.python import Python

def main(im):
    files_dir=str(Python.getPlatform().getApplication().getFilesDir())
    fileimg1=join(dirname(files_dir),"input.jpg")
    fileimg2=join(dirname(files_dir),"output.jpg")
    print("**********Reached Python**************")
    imgb = bytes(im, 'ascii')
    img_bytes = base64.decodebytes(imgb)
    with open(fileimg1, 'wb') as ip:
        ip.write(img_bytes)
    image = cv2.imread(fileimg1)
    image_file = Image.open(fileimg1) # open colour image
    image_file = image_file.convert('L') # convert image to black and white
    image_file.save(fileimg2)
    encoded_string = ''
    with open(fileimg2, "rb") as op:
        encoded_string = base64.b64encode(op.read())
    return ""+str(encoded_string,'utf-8')

