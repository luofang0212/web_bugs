#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv

with open('issues.csv','r',encoding='gbk') as fp:
    reader = csv.reader(fp)

    # 读取不包含title
    title = next(reader)
    for x in reader:
        print(x)