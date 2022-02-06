import io
import os
import base64
import bs4
from requests import Session 
from PIL import Image
import pytesseract

tesserDir = os.environ.get('OCR-Yande')
if not tesserDir:
    tesserDir = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


class Tesser():

    def __init__(self, path):

        
        self.path = path
        self.image: bytes = None
        self.image= open(path,'rb').read()

    def read_img(self):
        msg =base64.b64encode(self.image)
        msg = base64.b64decode(msg)
        buf = io.BytesIO(msg)
        img = Image.open(buf)

        pytesseract.pytesseract.tesseract_cmd = tesserDir
        _text = pytesseract.image_to_string(img,)
        text = _text.replace('\n', '').replace('\f', '')
        return(text)

for i in range(1,26):
    c=Tesser(f'slide/{i}.png')
    print(c.read_img())