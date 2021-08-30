#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv

# headers = ['name', 'age', 'classroom']
#
# values = [
#     ('zhangsan', 18, '101'),
#     ('李四', 17, '102'),
#     ('王五', 19, '103')
# ]
#
# with open('test.csv','w',newline='',encoding='utf-8') as fp:
#     writer = csv.writer(fp)
#     writer.writerow(headers)
#     writer.writerows(values)

headers = ['name', 'age', 'classroom']

values = [
    {"name":"zhangsan","age":18,"classroom":'101'},
    {"name": "zhangsan", "age": 14, "classroom": '102'},
    {"name": "zhangsan", "age": 15, "classroom": '103'},
]

with open('test_2.csv','w',newline='',encoding='utf-8') as fp:
    writer = csv.DictWriter(fp,headers)
    writer.writeheader()
    writer.writerow({"name":"zhangsan","age":18,"classroom":'101'})
    writer.writerows(values)
