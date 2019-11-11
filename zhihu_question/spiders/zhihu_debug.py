#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释
import urllib.parse
import json

import scrapy
from cocoNLP.extractor import extractor
from scrapy import Selector
from w3lib.html import remove_tags

from zhihu_question import Tools
from zhihu_question.items import ZhihuAnswerItem, ZhihuCommentItem, ZhihuAnswerEntity

# 执行方法，进入项目目录：
# scrapy crawl zhihu_debug
from zhihu_question.spiders import ZhihuAPIs

# 311464426: 广州的你，择偶的标准是怎样的？
# 275359100: 你择偶的标准是怎样的？
# 285906324: 有个漂亮女朋友是什么样的体验？


class ZhihuDebug(scrapy.Spider):

    # scrapy 配置
    name = "zhihu_debug"
    allowed_domains = ["www.zhihu.com"]

    def start_requests(self):
        # 参与用户关注的人
        for user_token in open('/Users/liu/Documents/zhihu/to_get_followee'):
            # 从文件读入一行会包含换行符
            user_token_no_warp = user_token.replace('\n', '')
            yield scrapy.Request(url=ZhihuAPIs.followees.format(user_token_no_warp),
                                 headers=Tools.gen_header(),
                                 callback=ZhihuAPIs.parse_followees,
                                 meta={'user_url_token': user_token_no_warp})

        # 用户简要消息（id -> url_token）
        # for user_id in open('/Users/liu/Documents/zhihu/user_ids'):
        #     # 从文件读入一行会包含换行符
        #     user_id_no_warp = user_id.replace('\n', '')
        #     yield scrapy.Request(url=ZhihuAPIs.user_info.format(user_id_no_warp),
        #                          headers=Tools.gen_header(),
        #                          callback=ZhihuAPIs.parse_user_info)


        # 关注问题的人
        # question_id = 311464426
        # yield scrapy.Request(url=ZhihuAPIs.question_followers.format(question_id),
        #                      headers=Tools.gen_header(),
        #                      callback=ZhihuAPIs.parse_question_followers,
        #                      meta={'question_id': question_id})

