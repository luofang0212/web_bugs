#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree

# html_element = etree.parse('qingsonbao.html')
parser = etree.HTMLParser(encoding='utf-8')
html_element = etree.parse('qingsonbao.html',parser=parser)
result = etree.tostring(html_element,encoding='utf-8').decode('utf-8')
print(result)
