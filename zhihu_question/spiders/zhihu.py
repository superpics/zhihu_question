#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释

from time import sleep
import json

import scrapy
from scrapy import Selector
from w3lib.html import remove_tags

from zhihu_question.items import ZhihuAnswerItem, ZhihuCommentItem


# 执行方法，进入项目目录：
# scrapy crawl zhihu



class zhihu(scrapy.Spider):
    # request 配置
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        # 'Referer': 'https://www.zhihu.com/question/311464426/answer/613785751',
        "Host": "www.zhihu.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }

    # 回答下的评论接口
    comment_template=r'https://www.zhihu.com/api/v4/answers/{0}/root_comments?order=normal&limit=20&offset=0&status=open';
    # 广州的你，择偶的标准是怎样的？
    url_template1 = r"https://www.zhihu.com/api/v4/questions/311464426/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=20&offset={0}&platform=desktop&sort_by=default"
    # 你择偶的标准是怎样的？
    url_template2 = r"https://www.zhihu.com/api/v4/questions/275359100/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=20&offset={0}&platform=desktop&sort_by=default"
    # 有个漂亮女朋友是什么样的体验？
    url_template3 = r"https://www.zhihu.com/api/v4/questions/285906324/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=20&offset={0}&platform=desktop&sort_by=default"



    # scrapy 配置
    name="zhihu"
    allowed_domains = ["www.zhihu.com"]

    def start_requests(self):
        offset = 0
        yield scrapy.Request(url=self.url_template1.format(offset), headers=self.headers, callback=self.parse_answer)

    # 解析某个问题下所有的回答
    def parse_answer(self, response):
        text = json.loads(response.body.decode(encoding='utf-8'))

        # 判断是否有下一页
        if not text['paging']['is_end']:
            # 遍历所有回答
            for answer in text['data']:
                yield self.gen_answer_item(answer)
            # 跳转到下一页
            sleep(1)
            yield scrapy.Request(url=text['paging']['next'], headers=self.headers, callback=self.parse_answer)
        else:
            # 退出
            self.crawler.engine.close_spider(self, '===> it is end')

    # 把每个回答封装成item对象
    def gen_answer_item(self, answer):
        item = ZhihuAnswerItem()

        # 获取剔除掉 html 标签的回答内容
        item['content'] = remove_tags(answer['content'])

        # 获取回答中的图片url
        img_urls = Selector(text=answer['content']).xpath("//img/@src").extract()
        for url in img_urls:
            if url.startswith("data"):
                img_urls.remove(url)
        item['image_urls'] = img_urls

        # 某种条件下，不可获取用户粉丝数（匿名用户才返回 follower_count，但是都为0）
        if "follower_count" in answer['author']:
            item['author_follower_count'] = int(answer['author']['follower_count'])
        else:
            item['author_follower_count'] = -1

        item['answer_id'] = str(answer['id'])
        item['created_time'] = int(answer['created_time'])
        item['updated_time'] = int(answer['updated_time'])
        item['voteup_count'] = int(answer['voteup_count'])
        item['comment_count'] = int(answer['comment_count'])
        item['author_name'] = answer['author']['name']
        item['author_url_token'] = answer['author']['url_token']
        item['author_headline'] = answer['author']['headline']
        item['author_gender'] = int(answer['author']['gender'])
        item['question_id'] = int(answer['question']['id'])
        item['question_title'] = answer['question']['title']
        item['question_created'] = answer['question']['created']
        item['question_updated_time'] = answer['question']['updated_time']

        # 处理该回答下的评论
        # if int(answer['comment_count']) > 0:
        #     # todo 此处为什么是用 return 不能是 yield
        #     yield scrapy.Request(url=self.comment_template.format(str(answer['id'])), headers=self.headers, callback=self.parse_comment)

        yield item

    # 解析某个问题下所有的评论
    def parse_comment(self, response):
        text = json.loads(response.body.decode(encoding='utf-8'))

        # 判断是否有下一页
        if not text['paging']['is_end']:
            # 遍历所有评论
            for comment in text['data']:
                yield self.gen_comment_item(comment)
            # 跳转到下一页
            yield scrapy.Request(url=text['paging']['next'], headers=self.headers, callback=self.parse_comment)

    def gen_comment_item(self, comment):
        item = ZhihuCommentItem()

        item['comment_id'] = str(comment['id'])
        item['comment_content'] = comment['content']
        item['comment_created_time'] = int(comment['created_time'])
        item['comment_vote_count'] = int(comment['vote_count'])
        item['child_comment_count'] = int(comment['child_comment_count'])
        item['author_url_token'] = comment['author']['member']['url_token']
        item['author_name'] = comment['author']['member']['name']
        item['author_gender'] = int(comment['author']['member']['gender'])

        return item
