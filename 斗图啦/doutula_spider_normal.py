#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lxml import etree
import re
import random
import os
from urllib import request
import warnings
warnings.simplefilter("ignore")

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 正常方式下载表情包

# 下载表情包到本地
def down_page_url():
    for x in range(1,101):
        url = 'https://www.doutula.com/photo/list/?page={0}'.format(x)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        }

        response = requests.get(url, headers=headers, verify=False)
        # print(response.text)

        with open('html/doutula_{0}.html'.format(x), 'wb') as fp:
            fp.write(response.content)
            print("{0} 成功下载到本地！！！".format(url))

def parse_page():
    imgs_info = []
    for i in range(1,73):
        html_file_name = 'html/doutula_{0}'.format(i)
        # print(html_file_name)
       # 读取72个html文件，进行解析
        parser= etree.HTMLParser(encoding='utf-8')
        html_element = etree.parse(html_file_name + '.html',parser=parser)
        # print(html_element)
        # 获取所有img
        imgs = html_element.xpath("//li[@class='list-group-item']//img[@referrerpolicy='no-referrer']")

        for img in imgs:
            img_dict = {}
            img_url = img.xpath('.//@data-backup')[0]

            img_name = img.xpath('.//@alt')[0]
            img_name = re.sub('[*\?？.。！@@!、/]+', '', img_name)
            if img_name == '':
                img_name = str(random.randint(100000, 20000000)) + str(random.randint(10, 200000))
            suffix = os.path.split(img_url)[1]
            name, ext = os.path.splitext(suffix)
            file_name = img_name + ext
            img_dict = {
                "img_url":img_url,
                "file_name":file_name
            }
            # print(img_dict)
            imgs_info.append(img_dict)
    return imgs_info

def start_down_imgs():
    imgs_info = parse_page()
    print(len(imgs_info))
    # print(imgs_info)
    for img in imgs_info:
        img_url = img['img_url']
        filename = img['file_name']
        request.urlretrieve(img_url,"images/" + filename)
        print("{0} 图片下载成功！！！".format(filename))

def start():
    # parse_page()
    start_down_imgs()


if __name__ == '__main__':
    start()
