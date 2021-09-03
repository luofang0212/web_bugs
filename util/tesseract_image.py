#!/usr/bin/env python
# -*- coding:utf-8 -*-


#!/usr/bin/env python
# -*- coding:utf-8 -*-

#OCR

import pytesseract
from PIL import Image

def imageCH_to_text(image_path):
    # 指定tesseract.exe所在的路径
    pytesseract.pytesseract.tesseract_cmd=r'D:\Program Files\Tesseract-OCR\tesseract.exe'

    # 打开图片
    image = Image.open(image_path)

    # 调用image_to_string将图片转换成文字,识别中文
    text = pytesseract.image_to_string(image,lang='chi_sim')

    return text

def imageEN_to_text(image_path):
    # 指定tesseract.exe所在的路径
    pytesseract.pytesseract.tesseract_cmd=r'D:\Program Files\Tesseract-OCR\tesseract.exe'

    # 打开图片
    image = Image.open(image_path)

    # 调用image_to_string将图片转换成文字,识别中文
    text = pytesseract.image_to_string(image,lang='eng')

    return text

if __name__ == '__main__':
    text = imageEN_to_text(r'D:\python_work\web_bugs\iamges\code_17058.jpeg')
    print(text)