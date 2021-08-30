#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import  BeautifulSoup

html_text = '''
<html>
<head><title>this is head</title></head>
<body>
<div class="table-responsive">
    <table class="table blue-table no-margin">
        <thead>
        <tr class="title">
            <th width="120">姓名</th>
            <th width="160">身份证</th>
            <th width="120">地区</th>
            <th width="120">服务</th>
            <th width="150">下单时间</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td><a href="https://www.baidu.com/s?wd=python">韦*彩</a></td>
            <td>11***************9</td>
            <td>上海</td>
            <td>社保</td>
            <td>2021-08-28</td>
        </tr>
        <tr>
            <td><a href="https://www.baidu.com/s?wd=python">常*彩</a></td>
            <td>61***************6</td>
            <td>上海</td>
            <td>社保</td>
            <td>2021-08-28</td>
        </tr>
        <tr>
            <td><a href="https://www.baidu.com/s?wd=java">渡*金</a></td>
            <td>11***************5</td>
            <td>上海</td>
            <td>社保</td>
            <td>2021-08-28</td>
        </tr>
        <tr>
            <td><a href="https://www.baidu.com/s?wd=net">大*旭</a></td>
            <td>61***************8</td>
            <td>上海</td>
            <td>社保</td>
            <td>2021-08-28</td>
        </tr>
        <tr>
             <td><a href="https://www.baidu.com/s?wd=php">倪*旭</a></td>
            <td>41***************2</td>
            <td>上海</td>
            <td>社保</td>
            <td>2021-08-28</td>
        </tr>
        </tbody>
    </table>
</div>
</body>
</html>

'''

# 1: 创建 BeautifulSoup 对象，使用lxml来进行解析
soup = BeautifulSoup(html_text,'lxml')
# print(soup.prettify())

# 获取html里tr标签下面的内容,soup.标签名
trs = soup.tr

# 获取所有子节点的迭代器
for i in trs.children:
    print(i)
