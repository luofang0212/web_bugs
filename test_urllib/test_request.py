#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request, parse
import ssl

# 全局去除证书验证
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.baidu.com'

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36"
}

req = request.Request(url, headers=headers)
res = request.urlopen(req)
# print(res.read())
r = res.read().decode('utf-8')
print(res.headers)
# print(r)
