#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree

# 1：获取HTML解析器
parser = etree.HTMLParser(encoding='utf-8')

# 2：将html文件进行解析
html_element = etree.parse('qingsonbao.html',parser=parser)

# 3:获得html里的元素信息
result = etree.tostring(html_element,encoding='utf-8').decode('utf-8')
# print(result)

# 根据解析器的内容，通过xpath提取文本内容

# 1: 获取所有的tr标签
# trs = html_element.xpath('//tr')
# for policy in trs:
#     print(policy)

# 2: 获取所有的a标签下的href信息
aList = html_element.xpath('//tr//a/@href')
for a in aList:
    print(a)

# 3: 获取所有的tr标签下的文本内容
trs = html_element.xpath('//tr[position()>1]')
for policy in trs:
    tds = policy.xpath('./td/text()')
    print(tds)








