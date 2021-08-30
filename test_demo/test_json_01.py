#!/usr/bin/env python
# -*- coding:utf-8 -*-


import json

books = [{
		"title": "唐诗三百首",
		"price": 18
	},
	{
		"title": "唐诗三百首",
		"price": 18
	}
]

# res = json.dumps(books,ensure_ascii=False)
# print(res)

with open('books.json','w',encoding='utf-8') as fp:
    json.dump(books,fp,ensure_ascii=False)