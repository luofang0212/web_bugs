#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request,parse

url = 'https://www.bilibili.com/video/BV1D3411q7GX?p=7'

# result = parse.urlsplit(url)
result = parse.urlparse(url)
print(result)

print(result.scheme)
print(result.netloc)
print(result.path)
print(result.query)
print(result.fragment)
