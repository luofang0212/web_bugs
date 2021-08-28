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
        '''
        <li class="ui-slide-item s" data-dstat-areaid="70_7" data-dstat-mode="click,expose" data-dstat-watch=".ui-slide-content" data-dstat-viewport=".screening-bd" data-title="新大头儿子和小头爸爸4：完美爸爸" data-release="2021" data-rate="5.0" data-star="25" data-trailer="https://movie.douban.com/subject/34913583/trailer" data-ticket="https://movie.douban.com/ticket/redirect/?movie_id=34913583" data-duration="80分钟" data-region="中国大陆" data-director="何澄" data-actors="董浩 / 鞠萍 / 陈怡" data-intro="" data-enough="true" data-rater="1416">
        '''
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
