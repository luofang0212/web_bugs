#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading

from queue import Queue

q = Queue(4)

# print(q.empty())
# print(q.full())
# q.put('a')
# q.put('b')
# q.put('c')

for x in range(4):
    q.put(x)

for x in range(4):
    print(q.get())