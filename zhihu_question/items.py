# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import peewee as peewee
import scrapy

# 1.连接数据库，传入必要参数数据库地址，用户名，密码，数据库名
db = peewee.MySQLDatabase('liu', **{'host': '127.0.0.1',
                                    'password': '123456',
                                    'port': 3307,
                                    'user': 'root'})


# 问题下回答封装类
class ZhihuAnswerItem(scrapy.Item):
    answer_id = scrapy.Field()
    content = scrapy.Field()
    image_urls = scrapy.Field()
    created_time = scrapy.Field()
    updated_time = scrapy.Field()
    voteup_count = scrapy.Field()
    comment_count = scrapy.Field()
    author_id = scrapy.Field()
    author_name = scrapy.Field()
    author_url_token = scrapy.Field()
    author_headline = scrapy.Field()
    author_gender = scrapy.Field()
    author_follower_count = scrapy.Field()
    question_id = scrapy.Field()
    question_title = scrapy.Field()
    question_created = scrapy.Field()
    question_updated_time = scrapy.Field()
    url = scrapy.Field()


# 问题下回答，回答的评论封装类（问题标题评论）
class ZhihuTitleCommentItem(scrapy.Item):
    question_id = scrapy.Field()
    comment_id = scrapy.Field()
    resource_type = scrapy.Field()
    comment_content = scrapy.Field()
    comment_created_time = scrapy.Field()
    comment_vote_count = scrapy.Field()
    child_comment_count = scrapy.Field()
    author_id = scrapy.Field()
    author_url_token = scrapy.Field()
    author_name = scrapy.Field()
    author_gender = scrapy.Field()


# 问题下回答，回答的评论封装类（回答评论）
class ZhihuCommentItem(scrapy.Item):
    question_id = scrapy.Field()
    answer_id = scrapy.Field()
    comment_id = scrapy.Field()
    resource_type = scrapy.Field()
    comment_content = scrapy.Field()
    comment_created_time = scrapy.Field()
    comment_vote_count = scrapy.Field()
    child_comment_count = scrapy.Field()
    author_id = scrapy.Field()
    author_url_token = scrapy.Field()
    author_name = scrapy.Field()
    author_gender = scrapy.Field()


# 问题下标题评论的子评论封装类
class ZhihuTitleChildrenCommentItem(scrapy.Item):
    question_id = scrapy.Field()
    father_comment_id = scrapy.Field()
    comment_id = scrapy.Field()
    vote_count = scrapy.Field()
    created_time = scrapy.Field()
    content = scrapy.Field()
    commentator_id = scrapy.Field()
    commentator_name = scrapy.Field()
    commentator_headline = scrapy.Field()
    commentator_gender = scrapy.Field()


# 问题下回答，回答的评论的子评论封装类
class ZhihuChildrenCommentItem(scrapy.Item):
    question_id = scrapy.Field()
    answer_id = scrapy.Field()
    father_comment_id = scrapy.Field()
    comment_id = scrapy.Field()
    vote_count = scrapy.Field()
    created_time = scrapy.Field()
    content = scrapy.Field()
    commentator_id = scrapy.Field()
    commentator_name = scrapy.Field()
    commentator_headline = scrapy.Field()
    commentator_gender = scrapy.Field()



# 用户简要信息
class ZhihuUserInfoItem(scrapy.Item):
    id = scrapy.Field()
    url_token = scrapy.Field()
    name = scrapy.Field()
    user_type = scrapy.Field()
    headline = scrapy.Field()
    gender = scrapy.Field()
    follower_count = scrapy.Field()
    answer_count = scrapy.Field()
    articles_count = scrapy.Field()


# 他关注的人
class ZhihuFolloweesItem(scrapy.Item):
    user_url_token = scrapy.Field()
    followee_id = scrapy.Field()
    followee_url_token = scrapy.Field()
    followee_name = scrapy.Field()
    followee_user_type = scrapy.Field()
    followee_headline = scrapy.Field()
    followee_gender = scrapy.Field()
    followee_follower_count = scrapy.Field()
    followee_answer_count = scrapy.Field()
    followee_articles_count = scrapy.Field()


# 关注他的人
class ZhihuFollowersItem(scrapy.Item):
    user_url_token = scrapy.Field()
    follower_id = scrapy.Field()
    follower_url_token = scrapy.Field()
    follower_name = scrapy.Field()
    follower_user_type = scrapy.Field()
    follower_headline = scrapy.Field()
    follower_gender = scrapy.Field()
    follower_follower_count = scrapy.Field()
    follower_answer_count = scrapy.Field()
    follower_articles_count = scrapy.Field()


# 关注问题的人
class ZhihuQuestionFollowersItem(scrapy.Item):
    question_id = scrapy.Field()
    url_token = scrapy.Field()
    user_type = scrapy.Field()
    answer_count = scrapy.Field()
    articles_count = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    headline = scrapy.Field()
    gender = scrapy.Field()
    follower_count = scrapy.Field()


# 问题的评论的子评论
class ZhihuQuestionCommentItem(scrapy.Item):
    question_id = scrapy.Field()
    answer_id = scrapy.Field()
    father_comment_id = scrapy.Field()
    comment_id = scrapy.Field()
    vote_count = scrapy.Field()
    created_time = scrapy.Field()
    content = scrapy.Field()
    commentator_id = scrapy.Field()
    commentator_name = scrapy.Field()
    commentator_headline = scrapy.Field()
    commentator_gender = scrapy.Field()


# 问题下回答（入库封装类）
class ZhihuAnswerEntity(peewee.Model):
    answer_id = peewee.IntegerField(verbose_name='回答id')
    content = peewee.CharField(verbose_name='回答内容', max_length=5000)
    created_time = peewee.BigIntegerField(verbose_name='回答创建时间', null=False, default=0)
    updated_time = peewee.BigIntegerField(verbose_name='回答修改时间', null=False, default=0)
    voteup_count = peewee.IntegerField(verbose_name='回答赞同数', null=False, default=0)
    comment_count = peewee.IntegerField(verbose_name='回答评论数', null=False, default=0)
    author_id = peewee.CharField(verbose_name='答者id', max_length=200)
    author_name = peewee.CharField(verbose_name='答者名字', max_length=100)
    author_url_token = peewee.CharField(max_length=200)
    author_headline = peewee.CharField(max_length=1000)
    author_gender = peewee.IntegerField(verbose_name='答者性别', default=-2)
    author_follower_count = peewee.IntegerField(verbose_name='答者粉丝数', default=-1)
    question_id = peewee.BigIntegerField(verbose_name='问题编号', null=False, default=0)
    question_title = peewee.CharField(verbose_name='问题标题', max_length=500)
    question_created = peewee.BigIntegerField(verbose_name='问题创建时间', null=False, default=0)
    question_updated_time = peewee.BigIntegerField(verbose_name='问题更改时间', null=False, default=0)
    url = peewee.CharField(verbose_name='来自url', max_length=1500)

    class Meta:
        database = db
        db_table = 'zhihu_answer'
        # 联合主键
        # primary_key = peewee.CompositeKey('question_id', 'answer_id')


# 问题下标题的评论（入库封装类）
class ZhihuTitleCommentEntity(peewee.Model):
    question_id = peewee.IntegerField(verbose_name='问题id')
    comment_id = peewee.IntegerField(verbose_name='评论id')
    resource_type = peewee.CharField(verbose_name='类型：question、answer', max_length=100)
    comment_content = peewee.CharField(verbose_name='评论内容', max_length=5000)
    comment_created_time = peewee.BigIntegerField(verbose_name='评论创建时间', null=False, default=0)
    comment_vote_count = peewee.IntegerField(verbose_name='评论赞同数', default=-1)
    child_comment_count = peewee.IntegerField(verbose_name='评论回复数', default=-1)
    author_id = peewee.CharField(verbose_name='评论者id', max_length=200)
    author_url_token = peewee.CharField(verbose_name='评论者token', max_length=200)
    author_name = peewee.CharField(verbose_name='评论者名字', max_length=100)
    author_gender = peewee.IntegerField(verbose_name='评论者性别', default=-2)

    class Meta:
        database = db
        db_table = 'zhihu_title_comment'
        # 联合主键
        # primary_key = peewee.CompositeKey('question_id', 'comment_id')


# 问题下标题的评论的子评论封装类
class ZhihuTitleChildrenCommentEntity(peewee.Model):
    question_id = peewee.IntegerField(verbose_name='问题id')
    father_comment_id = peewee.IntegerField(verbose_name='父评论id')
    comment_id = peewee.IntegerField(verbose_name='子评论id')
    vote_count = peewee.IntegerField(verbose_name='子评论赞同数')
    created_time = peewee.BigIntegerField(verbose_name='问题id')
    content = peewee.CharField(verbose_name='子评论内容', max_length=200)
    commentator_id = peewee.CharField(verbose_name='子评论者的id', max_length=200)
    commentator_name = peewee.CharField(verbose_name='子评论者的昵称签名', max_length=200)
    commentator_headline = peewee.CharField(verbose_name='子评论者的签名', max_length=200)
    commentator_gender = peewee.IntegerField(verbose_name='子评论者的性别')

    class Meta:
        database = db
        db_table = 'zhihu_title_children_comment'


# 问题下回答，回答的评论（入库封装类）
class ZhihuCommentEntity(peewee.Model):
    question_id = peewee.IntegerField(verbose_name='问题id')
    answer_id = peewee.IntegerField(verbose_name='回答id')
    comment_id = peewee.IntegerField(verbose_name='评论id')
    resource_type = peewee.CharField(verbose_name='类型：question、answer', max_length=100)
    comment_content = peewee.CharField(verbose_name='评论内容', max_length=5000)
    comment_created_time = peewee.BigIntegerField(verbose_name='评论创建时间', null=False, default=0)
    comment_vote_count = peewee.IntegerField(verbose_name='评论赞同数', default=-1)
    child_comment_count = peewee.IntegerField(verbose_name='评论回复数', default=-1)
    author_id = peewee.CharField(verbose_name='评论者id', max_length=200)
    author_url_token = peewee.CharField(verbose_name='评论者token', max_length=200)
    author_name = peewee.CharField(verbose_name='评论者名字', max_length=100)
    author_gender = peewee.IntegerField(verbose_name='评论者性别', default=-2)

    class Meta:
        database = db
        db_table = 'zhihu_comment'
        # 联合主键
        # primary_key = peewee.CompositeKey('question_id', 'answer_id', 'comment_id')


# 问题下回答，回答的评论的子评论封装类
class ZhihuChildrenCommentEntity(peewee.Model):
    question_id = peewee.IntegerField(verbose_name='问题id')
    answer_id = peewee.IntegerField(verbose_name='问题id')
    father_comment_id = peewee.IntegerField(verbose_name='父评论id')
    comment_id = peewee.IntegerField(verbose_name='子评论id')
    vote_count = peewee.IntegerField(verbose_name='子评论赞同数')
    created_time = peewee.BigIntegerField(verbose_name='问题id')
    content = peewee.CharField(verbose_name='子评论内容', max_length=200)
    commentator_id = peewee.CharField(verbose_name='子评论者的id', max_length=200)
    commentator_name = peewee.CharField(verbose_name='子评论者的昵称签名', max_length=200)
    commentator_headline = peewee.CharField(verbose_name='子评论者的签名', max_length=200)
    commentator_gender = peewee.IntegerField(verbose_name='子评论者的性别')

    class Meta:
        database = db
        db_table = 'zhihu_children_comment'
        # 联合主键（匿名用户的 token 为空）
        # primary_key = peewee.CompositeKey('question_id', 'url_token')


# 用户简要信息（入库封装类）
class ZhihuUserInfoEntity(peewee.Model):
    id = peewee.CharField(verbose_name='用户id', max_length=200)
    url_token = peewee.CharField(verbose_name='用户token', max_length=200)
    name = peewee.CharField(verbose_name='用户昵称', max_length=200)
    user_type = peewee.CharField(verbose_name='用户昵类型', max_length=200)
    headline = peewee.CharField(verbose_name='用户昵类型', max_length=500)
    gender = peewee.IntegerField(verbose_name='用户性别', default=-2)
    follower_count = peewee.IntegerField(verbose_name='用户粉丝数', null=False, default=0)
    answer_count = peewee.IntegerField(verbose_name='用户回答数', null=False, default=0)
    articles_count = peewee.IntegerField(verbose_name='用户文章数', null=False, default=0)

    class Meta:
        database = db
        db_table = 'zhihu_user_info'
        # 主键
        primary_key = peewee.CompositeKey('id', 'url_token')


# 他关注的人（入库封装类）
class ZhihuFolloweesEntity(peewee.Model):
    user_url_token = peewee.CharField(verbose_name='用户token', max_length=200)
    followee_id = peewee.CharField(verbose_name='他关注的人id', max_length=200)
    followee_url_token = peewee.CharField(verbose_name='他关注的人token', max_length=200)
    followee_name = peewee.CharField(verbose_name='他关注的人昵称', max_length=200)
    followee_user_type = peewee.CharField(verbose_name='他关注的人的类型', max_length=200)
    followee_headline = peewee.CharField(verbose_name='他关注的人的签名', max_length=200)
    followee_gender = peewee.IntegerField(verbose_name='他关注的人的性别', default=-2)
    followee_follower_count = peewee.IntegerField(verbose_name='他关注的人的粉丝数', null=False, default=0)
    followee_answer_count = peewee.IntegerField(verbose_name='他关注的人的回答数', null=False, default=0)
    followee_articles_count = peewee.IntegerField(verbose_name='他关注的人的文章数', null=False, default=0)

    class Meta:
        database = db
        db_table = 'zhihu_followees'
        # 联合主键
        primary_key = peewee.CompositeKey('user_url_token', 'followee_url_token')


# 关注他的人（入库封装类）
class ZhihuFollowersEntity(peewee.Model):
    user_url_token = peewee.CharField(verbose_name='用户token', max_length=200)
    follower_id = peewee.CharField(verbose_name='关注他的人id', max_length=200)
    follower_url_token = peewee.CharField(verbose_name='关注他的人token', max_length=200)
    follower_name = peewee.CharField(verbose_name='关注他的人昵称', max_length=200)
    follower_user_type = peewee.CharField(verbose_name='关注他的人的类型', max_length=200)
    follower_headline = peewee.CharField(verbose_name='关注他的人的签名', max_length=200)
    follower_gender = peewee.IntegerField(verbose_name='关注他的人的性别', default=-2)
    follower_follower_count = peewee.IntegerField(verbose_name='关注他的人的粉丝数', null=False, default=0)
    follower_answer_count = peewee.IntegerField(verbose_name='关注他的人的回答数', null=False, default=0)
    follower_articles_count = peewee.IntegerField(verbose_name='关注他的人的文章数', null=False, default=0)

    class Meta:
        database = db
        db_table = 'zhihu_followers'
        # 联合主键
        # primary_key = peewee.CompositeKey('user_url_token', 'follower_url_token')


# 关注知乎问题的人
class ZhihuQuestionFollowersEntity(peewee.Model):
    question_id = peewee.IntegerField(verbose_name='问题id')
    url_token = peewee.CharField(verbose_name='用户token', max_length=200)
    user_type = peewee.CharField(verbose_name='用户类型', max_length=200)
    answer_count = peewee.IntegerField(verbose_name='用户回答数', null=False, default=0)
    articles_count = peewee.IntegerField(verbose_name='文章数', null=False, default=0)
    id = peewee.CharField(verbose_name='id', max_length=200)
    name = peewee.CharField(verbose_name='昵称', max_length=200)
    headline = peewee.CharField(verbose_name='签名', max_length=200)
    gender = peewee.IntegerField(verbose_name='性别', default=-2)
    follower_count = peewee.IntegerField(verbose_name='粉丝数', null=False, default=0)

    class Meta:
        database = db
        db_table = 'zhihu_question_followers'
        # 联合主键（匿名用户的 token 为空）
        # primary_key = peewee.CompositeKey('question_id', 'url_token')






if __name__ == '__main__':
    # 自动建表
    # ZhihuAnswerEntity.create_table()
    # ZhihuCommentEntity.create_table()
    # ZhihuUserInfoEntity.create_table()
    # ZhihuFolloweesEntity.create_table()
    # ZhihuFollowersEntity.create_table()
    # ZhihuQuestionFollowersEntity.create_table()
    # ZhihuChildrenCommentEntity.create_table()
    # ZhihuTitleCommentEntity.create_table()
    # ZhihuTitleChildrenCommentEntity.create_table()
    ZhihuUserInfoEntity.create_table()

    # 插入记录
    # entity = ZhihuAnswerEntity.create(id=100, content='abc', image_urls='urls')
    # entity.save()
