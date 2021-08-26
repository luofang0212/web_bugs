#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib import parse

data ='name=%E7%88%AC%E8%99%AB&greet=hello+word&age=18'
res = parse.parse_qs(data)
res2 = parse.parse_qsl(data)
print(res)
print(res2)
#返回数据
{'name': ['爬虫'], 'greet': ['hello word'], 'age': ['18']}
[('name', '爬虫'), ('greet', 'hello word'), ('age', '18')]
# data = {'name':'爬虫','greet':'hello word','age':18}
# qs = parse.urlencode(data)
# print(qs)
# res = parse.parse_qs(qs)
# print(res)

