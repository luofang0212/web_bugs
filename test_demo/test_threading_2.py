#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time


class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('写代码中....{0}'.format(x))
            tn_name = threading.current_thread()
            print('线程名字:', tn_name)
            time.sleep(1)

class DrawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('画画中....{0}'.format(x))
            tn_name = threading.current_thread()
            print('线程名字:', tn_name)
            time.sleep(1)

def thread_run():
    t1 = CodingThread()
    t2 = DrawingThread()

    t1.start()
    t2.start()

if __name__ == '__main__':
    thread_run()