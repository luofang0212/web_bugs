
# 第三方库
# 解析html解析器
from lxml import etree
from bs4 import  BeautifulSoup  # BeautifulSoup4



# python自带库

import ssl
# 全局去除证书验证
ssl._create_default_https_context = ssl._create_unverified_context

# 数据处理
import json
import csv

import threading  #多线程
