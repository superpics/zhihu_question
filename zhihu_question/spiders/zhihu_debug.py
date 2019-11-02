#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释
import urllib.parse
import json

import scrapy
from scrapy import Selector
from w3lib.html import remove_tags

from zhihu_question import Tools
from zhihu_question.items import ZhihuAnswerItem, ZhihuCommentItem


# 执行方法，进入项目目录：
# scrapy crawl zhihu_debug
from zhihu_question.spiders import UserInfo


class ZhihuDebug(scrapy.Spider):

    # scrapy 配置
    name = "zhihu_debug"
    allowed_domains = ["www.zhihu.com"]

    def start_requests(self):
        return UserInfo.get_info("iconsider")
