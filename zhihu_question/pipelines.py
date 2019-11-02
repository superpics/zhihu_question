# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import random
import uuid

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

from zhihu_question.items import ZhihuAnswerEntity, ZhihuCommentEntity, ZhihuAnswerItem, ZhihuCommentItem, \
    ZhihuUserInfoItem, ZhihuFolloweesItem, ZhihuFollowersItem, ZhihuUserInfoEntity, ZhihuFolloweesEntity, \
    ZhihuFollowersEntity


class ZhihuQuestionPipeline(object):
    def process_item(self, item, spider):
        return item


# 用于保存回答信息到本地
class SaveContentToLocalPipeline(object):
    def process_item(self, item, spider):
        file = open("/tmp/scrapy/zobz.txt", "a", encoding='utf8')
        file.write(item['content'] + "\n")
        return item


# 用于保存回答信息到 mysql
class SaveContentToMysqlPipeline(object):
    def process_item(self, item, spider):
        # ZhihuCommentItem 的处理逻辑（主键重复插入则忽略冲突）
        if isinstance(item, ZhihuCommentItem):
            ZhihuCommentEntity.insert(
                question_id=item['question_id'],
                answer_id=item['answer_id'],
                comment_id=item['comment_id'],
                comment_content=item['comment_content'],
                comment_created_time=item['comment_created_time'],
                comment_vote_count=item['comment_vote_count'],
                child_comment_count=item['child_comment_count'],
                author_url_token=item['author_url_token'],
                author_name=item['author_name'],
                author_gender=item['author_gender']
            ).on_conflict_ignore().execute()
            return item
        # ZhihuAnswerItem 的处理逻辑（主键重复插入则忽略冲突）
        elif isinstance(item, ZhihuAnswerItem):
            ZhihuAnswerEntity.insert(
                answer_id=item['answer_id'],
                content=item['content'],
                created_time=item['created_time'],
                updated_time=item['updated_time'],
                voteup_count=item['voteup_count'],
                comment_count=item['comment_count'],
                author_name=item['author_name'],
                author_url_token=item['author_url_token'],
                author_headline=item['author_headline'],
                author_gender=item['author_gender'],
                author_follower_count=item['author_follower_count'],
                question_id=item['question_id'],
                question_title=item['question_title'],
                question_created=item['question_created'],
                question_updated_time=item['question_updated_time']
            ).on_conflict_ignore().execute()
            return item
        # ZhihuUserInfoItem 的处理逻辑（主键重复插入则忽略冲突）
        elif isinstance(item, ZhihuUserInfoItem):
            ZhihuUserInfoEntity.insert(
                id=item['id'],
                url_token=item['url_token'],
                name=item['name'],
                user_type=item['user_type'],
                headline=item['headline'],
                gender=item['gender'],
                follower_count=item['follower_count'],
                answer_count=item['answer_count'],
                articles_count=item['articles_count']
            ).on_conflict_ignore().execute()
            return item
        # ZhihuFolloweesItem 的处理逻辑（联合主键重复插入则忽略冲突）
        elif isinstance(item, ZhihuFolloweesItem):
            ZhihuFolloweesEntity.insert(
                user_url_token=item['user_url_token'],
                followee_id=item['followee_id'],
                followee_url_token=item['followee_url_token'],
                followee_name=item['followee_name'],
                followee_user_type=item['followee_user_type'],
                followee_headline=item['followee_headline'],
                followee_gender=item['followee_gender'],
                followee_follower_count=item['followee_follower_count'],
                followee_answer_count=item['followee_answer_count'],
                followee_articles_count=item['followee_articles_count']
            ).on_conflict_ignore().execute()
            return item
        # ZhihuFollowersItem 的处理逻辑（联合主键重复插入则忽略冲突）
        elif isinstance(item, ZhihuFollowersItem):
            ZhihuFollowersEntity.insert(
                user_url_token=item['user_url_token'],
                follower_id=item['follower_id'],
                follower_url_token=item['follower_url_token'],
                follower_name=item['follower_name'],
                follower_user_type=item['follower_user_type'],
                follower_headline=item['follower_headline'],
                follower_gender=item['follower_gender'],
                follower_follower_count=item['follower_follower_count'],
                follower_answer_count=item['follower_answer_count'],
                follower_articles_count=item['follower_articles_count']
            ).on_conflict_ignore().execute()
            return item


# 继承ImagesPipeline，实现下载图片
class ImgPipeline(ImagesPipeline):
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "upgrade-insecure-requests": "1",
        "User-Agent": random.choice(user_agent_list)
    }

    # 发送图片下载请求
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url, meta={'item': item, 'referer': image_url, 'headers': self.headers})

    # 这个方法是在图片将要被存储的时候调用，来获取这个图片存储的路径
    def file_path(self, request, response=None, info=None):
        img_file = str(uuid.uuid1()) + ".jpg"
        return img_file