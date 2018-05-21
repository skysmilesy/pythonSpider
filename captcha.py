#-*- coding:utf-8 -*-
# Author:yan.shao

import requests
from bs4 import BeautifulSoup
import base64
from PIL import Image
from io import BytesIO
import pytesseract
url='http://example.webscraping.com/places/default/user/register'
response=requests.get(url)
soup=BeautifulSoup(response.text, 'html.parser')
li=soup.select('#recaptcha > img')
src=li[0].get('src')
src=src.replace('data:image/png;base64,','')
# print(src)
binary=base64.b64decode(src)
# with open('1.jpg','wb') as f:
#     f.write(binary)
# image=Image.open('1.jpg')
image=Image.open(BytesIO(binary))
image.save('1.jpg')
pytesseract.pytesseract.tesseract_cmd=r'E:\Program Files (x86)\Tesseract-OCR\tesseract'
#对图片进行处理，提取验证码的有效信息。
image=image.convert('L')
#将图片进行二值化
# def manage(pixel):
#     if pixel == 0:
#         return pixel
#     else:
#         return 255
# image.point(manage)
image.point(lambda x:0 if x==0 else 255)
image.show()



