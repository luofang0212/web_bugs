#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree

text = '''
        <tr>
            <th width="120">姓名</th>
            <th width="160">身份证</th>
            <th width="120">地区</th>
            <th width="120">服务</th>
            <th width="150">下单时间</th>
        </tr>                              
'''

# 利用etree.HTML()，将字符串转换成html文件
html_element = etree.HTML(text)

# 按字符串序列转换html文档
result = etree.tostring(html_element,encoding='utf-8').decode('utf-8')
print(result)


