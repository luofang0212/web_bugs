#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time

gLock = threading.Lock()
ticks = 0

def coding():
    global ticks
    gLock.acquire() # 加锁
    for x in range(100000):
        # print('写代码中....{0}'.format(x))
        ticks += 1
    gLock.release()  # 释放锁
    print("coding ticks的值：{0}".format(ticks))

def main():
    thread_1 = threading.Thread(target=coding)
    thread_1.start()


if __name__ == '__main__':
    main()
