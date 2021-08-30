#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
   获取豆瓣电影里的正在热映的影片数据
'''
from lxml import etree


# 1：解析html
# 2: 获取正在热映的电影列表,提取电影内容

# 1：解析html
def parser():
    parser = etree.HTMLParser(encoding='utf-8')
    html_element = etree.parse('douban.html', parser=parser)
    return html_element


# result = etree.tostring(html_element,encoding='utf-8').decode('utf-8')
# print(result)

# 2: 获取正在热映的电影列表，提取热映影片详情内容
def get_movie_url():
    html_element = parser()
    # 通过xpath去获取所有的正在热映的列表
    hot_movies = html_element.xpath("//div[@class='screening-bd']//ul[@class='ui-slide-content']")[0]
    hots = hot_movies.xpath("./li[@class='ui-slide-item']")[0:33]
    # print(len(hots))
    hot_movies_data = []

    for hot in hots:
        hots_data = {}

        title = hot.xpath("./@data-title")[0].strip()
        release = hot.xpath("./@data-release")[0].strip()
        rate = hot.xpath("./@data-rate")[0].strip() + '分'
        duration = hot.xpath("./@data-duration")[0].strip()
        region = hot.xpath("./@data-region")[0].strip()
        director = hot.xpath("./@data-director")[0].strip()
        actors = hot.xpath("./@data-actors")[0].strip()
        detail_url = hot.xpath(".//li[@class='poster']/a/@href")[0]

        # print(detail_url)
        hots_data = {
            "title": title,
            "release": release,
            "rate": rate,
            "duration":duration,
            "region":region,
            "director":director,
            "actors":actors,
            "detail_url":detail_url

        }

        hot_movies_data.append(hots_data)

    print(hot_movies_data)
    return hot_movies_data


def start():
    get_movie_url()


if __name__ == '__main__':
    start()
