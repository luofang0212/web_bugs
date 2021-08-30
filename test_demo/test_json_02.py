#!/usr/bin/env python
# -*- coding:utf-8 -*-


import json

# books_str = '''
# [{
# 		"title": "唐诗三百首",
# 		"price": 18
# 	},
# 	{
# 		"title": "唐诗三百首",
# 		"price": 18
# 	}
# ]
# '''
#
# books_json = json.loads(books_str)
# print(books_json)

with open('books.json','r',encoding='utf-8') as fp:
	books = json.load(fp)
print(books)