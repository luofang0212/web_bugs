#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''使用BeautifulSoup4'''

from bs4 import BeautifulSoup
import requests
from lxml import etree
import html5lib
import csv

'''
1: 爬取网页,下载到本地
2：获取 table里的城市和最低温度
'''
def down_url():

    urls = ['hb','db','hd','hz','hn','xb','xn','gat']

    for x in range(0,8):
        url_index = urls[x]
        url = 'http://www.weather.com.cn/textFC/{0}.shtml'.format(url_index)
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36"
        }

        # 1: 下载网页
        response = requests.get(url,headers=headers)
        with open('{0}.html'.format(url_index),'wb') as fp:
            fp.write(response.content)
            print("{0}页面成功下载到本地！！！".format(url))


def parse():
    urls = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn', 'gat']
    infos = []
    for x in range(0,8):
        url_index = urls[x]
        # 1：获取已下载好的页面
        parser = etree.HTMLParser(encoding='utf-8')
        html_element = etree.parse('{0}.html'.format(url_index),parser=parser)
        html_text = etree.tostring(html_element,encoding='utf-8').decode('utf-8')
        # 1：创建解析器，由于gat页面里的table标签不规范，所以使用html5lib解析器
        soup = BeautifulSoup(html_text,'html5lib')
        # soup = BeautifulSoup(html_text, 'lxml')
        # print(soup.prettify())

        # 分析 城市和最低温度 在table下面的tr里面的td
        # 2:获取当前页面所有的table
        conMidtab = soup.find('div',class_='conMidtab')
        tables = conMidtab.find_all('table')
        # print(len(tables))
        for table in tables:
            # print(table)
            info = {}
            trs = table.find_all('tr')[2:]
            for tr in trs:
                tds = tr.find_all('td')
                # 获取城市信息
                city_td = tds[0]
                city = list(city_td.stripped_strings)[0] # stripped_strings返回的是一个生成器，需要放在列表里
                # print(city)
                # 获取城市最低温度,在倒序第二个td上
                min_temperature_td = tds[-2]
                min_temperature = min_temperature_td.string
                # print(min_temperature)
                info = {
                    "city":city,
                    "min_temperature":min_temperature
                }
                # print(info)
            infos.append(info)
    return infos

def write_csv():
    headers = ['city','min_temperature']
    infos = parse()
    with open('城市最低温度.csv','w',newline='',encoding='utf-8') as fp:
        writer = csv.DictWriter(fp,headers)
        writer.writeheader()
        writer.writerows(infos)

def start():
    write_csv()


if __name__ == '__main__':
    start()