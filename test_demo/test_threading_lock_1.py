#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time
import random

gLock = threading.Lock()
gMoney = 1000
# 生产次数
gtimes = 0


# 生产者
class ProductThread(threading.Thread):
    def run(self):
        global gMoney
        global gLock
        global gtimes
        while True:
            # 挣钱
            money = random.randint(10, 1000)
            gLock.acquire()  # 加锁
            if gtimes >= 10:
                gLock.release()
                print('{0}这次没能力挣钱了，gMoney总共为：{1}元，我们就别花钱了！！！！'.format(t_name,  gMoney))
                break
            gMoney = gMoney + money
            t_name = threading.current_thread()
            print('{0}这次挣了{1}元，gMoney总共为：{2}元'.format(t_name, money, gMoney))
            gtimes += 1
            time.sleep(0.5)
            gLock.release()  # 释放锁


# 消费者
class ConsumerThread(threading.Thread):
    def run(self):
        global gMoney
        global gLock
        global gtimes
        while True:
            # 花钱
            money = random.randint(100, 1000)
            gLock.acquire()  # 加锁
            if gMoney >= money:
                gMoney = gMoney - money
                t_name = threading.current_thread()
                print('{0}准备消费{1}元，gMoney总共为：{2}元，消费成功'.format(t_name, money, gMoney))
            else:
                if gtimes >= 10:
                    gLock.release()  # 释放锁
                    t_name = threading.current_thread()
                    print('{0}准备消费{1}元，gMoney总共为：{2}元,余额不足,没能力挣钱了'.format(t_name, money, gMoney))
                    break
                else:
                    t_name = threading.current_thread()
                    print('{0}准备消费{1}元，gMoney总共为：{2}元,余额不足,继续挣钱去'.format(t_name, money, gMoney))
            gLock.release()  # 释放锁
            time.sleep(0.5)


def main():
    for i in range(3):
        pt = ProductThread(name='生产者')
        pt.start()

    for i in range(5):
        ct = ConsumerThread(name='消费者')
        ct.start()


if __name__ == '__main__':
    main()
