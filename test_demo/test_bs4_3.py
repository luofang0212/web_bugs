#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import  BeautifulSoup

html_text = '''

    <table class="table blue-table no-margin">
        <thead>
        <tr class="title" >
            <th class="event" width="120">姓名</th>
            <th class="event" width="160">身份证</th>
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
        <tr class="event">
            <td><a href="https://www.baidu.com/s?wd=python">常*彩</a></td>
            <td class="event">61***************6</td>
            <td class="event">上海</td>
            <td>社保</td>
            <td>2021-08-28</td>
        </tr>
        <tr class="event">
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


'''

# 1: 创建 BeautifulSoup 对象，使用lxml来进行解析
soup = BeautifulSoup(html_text,'lxml')

# 获取所有的tr标签
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)

# 获取第二个的tr标签
# tr = soup.find_all('tr',limit=2)[1]
# print(tr)

# # 获取所有class=event的tr标签
# trs = soup.find_all('tr',attrs={"class":"event"})
# for tr in trs:
#     print(tr)

# 获取所有a标签，有href属性
# aList = soup.find_all('a')
# for a in aList:
#     # print(a)
#     # 方式一
#     href = a['href']
#     #方式二
#     href = a.attrs['href']
#     print(href)

# 获取所有的td里的文本（纯文本）
trs = soup.find_all('tr')[1:]
for x in trs:
    tds = soup.find_all('td')

    name = tds[0]
    # no = tds[1]
    # print(no.string)
    # print(name.strings)
    # print(name.get_text)
    # print(no.stripped_strings)