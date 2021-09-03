#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pytesseract
from PIL import Image
import requests
from urllib import request
import json,base64
from lxml import etree
import re
import random
import time

def image_code():

    url = r'http://172.16.127.100:37737/account/login'
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "Host": "172.16.127.100:37737"
    }
    response = requests.get(url,headers=headers)
    # 返回的是图片是base64
    with open('1.html','wb') as fp:
        fp.write(response.content)

    parser = etree.HTMLParser(encoding='utf-8')
    html_elemet = etree.parse('1.html',parser=parser)

    # 获取验证码
    imge = html_elemet.xpath("//img[@id='captcha-image']/@src")[0]
    imge = re.sub(r'(.*,)+','',imge)
    # print(imge)

    num = random.randint(1000,100000)
    image_path = 'code_{0}.png'.format(num)
    # 将base64转换成图片
    with open(image_path,'wb') as fp:
        fp.write(base64.b64decode(imge))
        print(image_path)

    time.sleep(2)
    # 指定tesseract.exe所在的路径
    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

    # 打开图片
    image = Image.open(image_path)

    # 调用image_to_string将图片转换成文字
    text = pytesseract.image_to_string(image,lang='chi_sim')
    print(text)


if __name__ == '__main__':
    image_code()