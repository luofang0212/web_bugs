#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib import request

res = request.urlopen('http://www.baidu.com/')
print(res.read())
# print(res.readline())
# print(res.readlines())
# print(res.getcode())