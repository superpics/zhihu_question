#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释


# 知乎用户信息
import json
import urllib

import scrapy

from zhihu_question import Tools


# 用户简要信息
from zhihu_question.items import ZhihuUserInfoItem, ZhihuFolloweesItem, ZhihuFollowersItem

user_info = r'https://www.zhihu.com/api/v4/members/{0}?include=allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics';
# 动态, session_id after_id
activities = r'https://www.zhihu.com/api/v4/members/{0}/activities?limit=7&session_id=1059565714700111872&after_id=1570103670&desktop=True'
# 想法
pins = r'https://www.zhihu.com/api/v4/members/{0}/pins?offset=0&limit=20&includes=data[*].upvoted_followees,admin_closed_comment'
# 提问
questions = r'https://www.zhihu.com/api/v4/members/{0}/questions?include=data[*].created,answer_count,follower_count,author,admin_closed_comment&offset=0&limit=20'
# 专栏
column_contributions = r'https://www.zhihu.com/api/v4/members/{0}/column-contributions?include=data[*].column.intro,followers,articles_count&offset=0&limit=20'
# 回答列表
answers = r'https://www.zhihu.com/api/v4/members/{0}/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,mark_infos,created_time,updated_time,review_info,excerpt,is_labeled,label_info,relationship.is_authorized,voting,is_author,is_thanked,is_nothelp,is_recognized;data[*].author.badge[?(type=best_answerer)].topics;data[*].question.has_publishing_draft,relationship&offset=0&limit=20&sort_by=created'
# 他关注的人
followees = r'https://www.zhihu.com/api/v4/members/{0}/followees?include=data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics&offset=0&limit=20'
# 关注他的人
followers = r'https://www.zhihu.com/api/v4/members/{0}/followers?include=data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics&offset=0&limit=20'


def get_info(url_token):
    # return do_user_info(url_token)
    # return do_followees(url_token)
    return do_followers(url_token)


def do_user_info(url_token):
    yield scrapy.Request(url=user_info.format(url_token), headers=Tools.gen_header(), callback=parse_user_info)


def parse_user_info(response):
    text = json.loads(response.body.decode(encoding='utf-8'))

    item = ZhihuUserInfoItem()
    item['id'] = text['id']
    item['url_token'] = text['url_token']
    item['name'] = text['name']
    item['user_type'] = text['user_type']
    item['headline'] = text['headline']
    item['gender'] = text['gender']
    item['follower_count'] = text['follower_count']
    item['answer_count'] = text['answer_count']
    item['articles_count'] = text['articles_count']
    return item


def do_followees(url_token):
    yield scrapy.Request(url=followees.format(url_token), headers=Tools.gen_header(), callback=parse_followees,
                         # 传参到回调函数
                         meta={'user_url_token': url_token})


def parse_followees(response):
    text = json.loads(response.body.decode(encoding='utf-8'))
    user_url_token = response.meta['user_url_token']

    # 遍历所有评论
    for followee in text['data']:
        item = ZhihuFolloweesItem()
        item['user_url_token'] = user_url_token
        item['followee_id'] = followee['id']
        item['followee_url_token'] = followee['url_token']
        item['followee_name'] = followee['name']
        item['followee_user_type'] = followee['user_type']
        item['followee_headline'] = followee['headline']
        item['followee_gender'] = followee['gender']
        item['followee_follower_count'] = followee['follower_count']
        item['followee_answer_count'] = followee['answer_count']
        item['followee_articles_count'] = followee['articles_count']
        yield item

    # 判断是否有下一页
    if not text['paging']['is_end']:
        # 特别处理下一页的 url，缺失 /api/v4
        url_part = urllib.parse.urlparse(text['paging']['next'])
        next_page = "https://www.zhihu.com/api/v4%s?%s" % (url_part.path, url_part.query)
        # 跳转到下一页
        yield scrapy.Request(url=next_page, headers=Tools.gen_header(), callback=parse_followees,
                             meta={'user_url_token': user_url_token})


def do_followers(url_token):
    yield scrapy.Request(url=followers.format(url_token), callback=parse_followers,
                         # 传参到回调函数
                         meta={'user_url_token': url_token})


def parse_followers(response):
    text = json.loads(response.body.decode(encoding='utf-8'))
    user_url_token = response.meta['user_url_token']

    # 遍历所有评论
    for follower in text['data']:
        item = ZhihuFollowersItem()
        item['user_url_token'] = user_url_token
        item['follower_id'] = follower['id']
        item['follower_url_token'] = follower['url_token']
        item['follower_name'] = follower['name']
        item['follower_user_type'] = follower['user_type']
        item['follower_headline'] = follower['headline']
        item['follower_gender'] = follower['gender']
        item['follower_follower_count'] = follower['follower_count']
        item['follower_answer_count'] = follower['answer_count']
        item['follower_articles_count'] = follower['articles_count']
        yield item

    # 判断是否有下一页
    if not text['paging']['is_end']:
        # 特别处理下一页的 url，缺失 /api/v4
        url_part = urllib.parse.urlparse(text['paging']['next'])
        next_page = "https://www.zhihu.com/api/v4%s?%s" % (url_part.path, url_part.query)
        # 跳转到下一页
        yield scrapy.Request(url=next_page, callback=parse_followers,
                             meta={'user_url_token': user_url_token})




