#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释

from time import sleep
import json

import scrapy
from scrapy import Selector
from w3lib.html import remove_tags

from zhihu_question.items import ZhihuQuestionItem


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

    # 广州的你，择偶的标准是怎样的？
    url_template1 = r"https://www.zhihu.com/api/v4/questions/311464426/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=20&offset={0}&platform=desktop&sort_by=default"
    # 你择偶的标准是怎样的？
    url_template2 = r"https://www.zhihu.com/api/v4/questions/275359100/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=5&offset={0}&platform=desktop&sort_by=default"
    # 有个漂亮女朋友是什么样的体验？
    url_template3 = r"https://www.zhihu.com/api/v4/questions/285906324/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=5&offset=8&platform=desktop&sort_by=default"


    # scrapy 配置
    name="zhihu"
    allowed_domains = ["www.zhihu.com"]

    def start_requests(self):
        for offset in range(0, 50000, 20):
            yield scrapy.Request(url=self.url_template2.format(offset), headers=self.headers, callback=self.parse)
            print(offset)
            sleep(1)

    def parse(self, response):
        text = json.loads(response.body.decode(encoding='utf-8'))

        if not text['paging']['is_end']:
            for answer in text['data']:
                item = ZhihuQuestionItem()

                # 获取剔除掉 html 标签的回答内容
                item['content'] = remove_tags(answer['content'])

                # 获取回答中的图片url
                img_urls = Selector(text=answer['content']).xpath("//img/@src").extract()
                for url in img_urls:
                    if url.startswith("data"):
                        img_urls.remove(url)
                item['image_urls'] = img_urls

                # 获取id
                item['id'] = str(answer['id'])

                yield item
        else:
            self.crawler.engine.close_spider(self, '===> it is end')