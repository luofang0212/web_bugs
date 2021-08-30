#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time

def coding():
    for x in range(3):
        print('写代码中....{0}'.format(x))
        tn_name = threading.current_thread()
        print('线程名字:', tn_name)
        time.sleep(1)

def drawing():
    for x in range(3):
        print('画画中....{0}'.format(x))
        tn_name = threading.current_thread()
        print('线程名字:', tn_name)
        time.sleep(1)

def main():
    thread_1 = threading.Thread(target=coding)
    thread_2 = threading.Thread(target=drawing)

    thread_1.start()
    thread_2.start()
    tn = threading.enumerate()
    print('线程数:',tn)

    tn_name = threading.current_thread()
    print('线程名字:', tn_name)
if __name__ == '__main__':
    main()