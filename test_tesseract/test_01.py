#!/usr/bin/env python
# -*- coding:utf-8 -*-

#OCR

import pytesseract
from PIL import Image

# 指定tesseract.exe所在的路径
pytesseract.pytesseract.tesseract_cmd=r'D:\Program Files\Tesseract-OCR\tesseract.exe'

# 打开图片
image = Image.open("8.png")


# 调用image_to_string将图片转换成文字,识别中文
text = pytesseract.image_to_string(image,lang='chi_sim')


print(text)


