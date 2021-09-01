#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

def save_url():
    url = 'https://so.gushiwen.cn/shiwens/default.aspx?page=1&tstr=&astr=&cstr=&xstr='

    headers = {
        "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36'
    }

    response = requests.get(url, headers)
    with open('shiwens.html', 'wb') as fp:
        fp.write(response.content)
        print('{0}成功下载到本地！！！'.format(url))

if __name__ == '__main__':
    save_url()