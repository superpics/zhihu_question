#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释
import json
import urllib.parse


def test():
    for i in (1, 2, 3):
        yield i
        yield str(i)
    yield 9


if __name__ == "__main__":
    url_part = urllib.parse.urlparse('https://www.zhihu.com/answers/607521879/root_comments?limit=20&offset=20&order=normal&status=open')
    print(url_part.scheme)
    print(url_part.netloc)
    print(url_part.path)
    print(url_part.params)
    print(url_part.query)

    print("https://www.zhihu.com/api/v4%s?%s" % (url_part.path, url_part.query))







