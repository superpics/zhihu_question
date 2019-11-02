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
# scrapy crawl zhihu
from zhihu_question.spiders import UserInfo


class zhihu(scrapy.Spider):
    # 回答下的评论接口
    comment_template = r'https://www.zhihu.com/api/v4/answers/{0}/root_comments?order=normal&limit=20&offset=0&status=open';
    # 广州的你，择偶的标准是怎样的？
    url_template1 = r"https://www.zhihu.com/api/v4/questions/311464426/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=20&offset={0}&platform=desktop&sort_by=default"
    # 你择偶的标准是怎样的？
    url_template2 = r"https://www.zhihu.com/api/v4/questions/275359100/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=20&offset={0}&platform=desktop&sort_by=default"
    # 有个漂亮女朋友是什么样的体验？
    url_template3 = r"https://www.zhihu.com/api/v4/questions/285906324/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=20&offset={0}&platform=desktop&sort_by=default"

    # scrapy 配置
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]

    def start_requests(self):
        offset = 0
        yield scrapy.Request(url=self.url_template2.format(offset), headers=Tools.gen_header(), callback=self.parse_answer)

    # 解析某个问题下所有的回答
    def parse_answer(self, response):
        text = json.loads(response.body.decode(encoding='utf-8'))

        # 判断是否有下一页
        if not text['paging']['is_end']:
            # 遍历所有回答
            for answer in text['data']:
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
                if int(answer['comment_count']) > 0:
                    yield scrapy.Request(url=self.comment_template.format(str(answer['id'])),
                                         headers=Tools.gen_header(), callback=self.parse_comment,
                                         # 传参到回调函数
                                         meta={'answer_id': str(answer['id']),
                                               'question_id': int(answer['question']['id'])})

                # 回答者简要信息
                url_token = answer['author']['url_token']
                yield scrapy.Request(url=UserInfo.user_info.format(url_token),
                                     headers=Tools.gen_header(), callback=UserInfo.parse_user_info)
                # 回答者关注的人
                yield scrapy.Request(url=UserInfo.followees.format(url_token),
                                     headers=Tools.gen_header(),
                                     callback=UserInfo.parse_followees,
                                     # 传参到回调函数
                                     meta={'user_url_token': url_token})
                # 关注回答者的人
                yield scrapy.Request(url=UserInfo.followers.format(url_token),
                                     callback=UserInfo.parse_followers,
                                     # 传参到回调函数
                                     meta={'user_url_token': url_token})

                yield item

            # 跳转到下一页
            yield scrapy.Request(url=text['paging']['next'], headers=Tools.gen_header(), callback=self.parse_answer)
        else:
            # 退出
            self.crawler.engine.close_spider(self, '===> zhihu scrapy end !!!')

    # 解析某个问题回答下所有的评论
    def parse_comment(self, response):
        text = json.loads(response.body.decode(encoding='utf-8'))

        # meta 由 request 传入
        answer_id = response.meta['answer_id']
        question_id = response.meta['question_id']
        # 遍历所有评论
        for comment in text['data']:
            item = ZhihuCommentItem()
            item['answer_id'] = answer_id
            item['question_id'] = question_id
            item['comment_id'] = str(comment['id'])
            item['comment_content'] = remove_tags(comment['content'])
            item['comment_created_time'] = int(comment['created_time'])
            item['comment_vote_count'] = int(comment['vote_count'])
            item['child_comment_count'] = int(comment['child_comment_count'])
            item['author_url_token'] = comment['author']['member']['url_token']
            item['author_name'] = comment['author']['member']['name']
            item['author_gender'] = int(comment['author']['member']['gender'])

            # 回答者简要信息
            author_url_token = comment['author']['member']['url_token']
            yield scrapy.Request(url=UserInfo.user_info.format(author_url_token),
                                 headers=Tools.gen_header(), callback=UserInfo.parse_user_info)
            # 回答者关注的人
            yield scrapy.Request(url=UserInfo.followees.format(author_url_token),
                                 headers=Tools.gen_header(),
                                 callback=UserInfo.parse_followees,
                                 # 传参到回调函数
                                 meta={'user_url_token': author_url_token})
            # 关注回答者的人
            yield scrapy.Request(url=UserInfo.followers.format(author_url_token),
                                 callback=UserInfo.parse_followers,
                                 # 传参到回调函数
                                 meta={'user_url_token': author_url_token})

            yield item

        # 判断是否有下一页
        if not text['paging']['is_end']:
            # 特别处理回答下评论的下一页 url，缺失 /api/v4
            url_part = urllib.parse.urlparse(text['paging']['next'])
            next_page = "https://www.zhihu.com/api/v4%s?%s" % (url_part.path, url_part.query)

            # 跳转到下一页
            yield scrapy.Request(url=next_page, headers=Tools.gen_header(), callback=self.parse_comment,
                                 meta={'answer_id': answer_id, 'question_id': question_id})
