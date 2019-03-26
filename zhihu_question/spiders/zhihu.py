#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释

import html
from time import sleep
import json

import scrapy


class DmozItem(scrapy.Item):
    content = scrapy.Field()


class zhihu(scrapy.Spider):
    # request 配置
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Host": "www.zhihu.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }

    url_template = r"https://www.zhihu.com/api/v4/questions/311464426/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=5&offset={0}&platform=desktop&sort_by=default"
    url_template_test = r"https://www.zhihu.com/api/v4/questions/311464426/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=5&offset={0}&platform=desktop&sort_by=default"

    # scrapy 配置
    name="zhihu"
    allowed_domains = ["www.zhihu.com"]

    def start_requests(self):
        for offset in range(3):
            yield scrapy.Request(url=self.url_template.format(offset), headers=self.headers, callback=self.parse)
            sleep(1)
        # yield scrapy.Request(url=self.url_template_test.format(5), headers=self.headers, callback=self.parse)

    def parse(self, response):
        # # html转义，如: &lt; => <
        # convert_html = html.unescape(response.body.decode(encoding='utf-8'))
        # # unicode转字符，如：\u003cbr/\u003e => <br>
        # convert_unicode = eval("'''" + convert_html + "'''")
        # print(convert_unicode)
        # text = json.loads(convert_unicode)
        # print(text)

        text = json.loads(response.body.decode(encoding='utf-8'))
        print(text)