#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


text = '0123456'

ret = re.search(r'\d+',text)
print(ret.group())

