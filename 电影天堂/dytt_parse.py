#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from io import StringIO, BytesIO
import gzip
from gzip import GzipFile

url = 'https://www.dy2018.com/1/'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    "Accept-Encoding": "gzip"
}

response = requests.get(url, headers=headers, verify=False)
data = response.content



with open('dytt.html', 'wb') as fp:
    fp.write(response.content)
