#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time

ticks = 0
def coding():
    global ticks
    for x in range(111000):
        # print('写代码中....{0}'.format(x))
        ticks += 1
    print("coding ticks的值：{0}".format(ticks))

def drawing():
    global ticks
    for x in range(1000):
        # print('画画中....{0}'.format(x))
        ticks += 1
    print("drawing ticks的值：{0}".format(ticks))

def main():
    thread_1 = threading.Thread(target=coding)
    # thread_2 = threading.Thread(target=drawing)

    thread_1.start()
    # thread_2.start()

if __name__ == '__main__':
    main()

# 数据返回