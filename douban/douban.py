#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    爬取豆瓣电影里的正在热映的电影信息
'''
import requests

url = 'https://movie.douban.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

# 获取豆瓣电影地址
response = requests.get(url,headers=headers,verify=False)
# print(response.text)

with open('douban.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))


