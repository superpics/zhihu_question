# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import peewee as peewee
import scrapy


class ZhihuAnswerItem(scrapy.Item):
    id = scrapy.Field()
    content = scrapy.Field()
    image_urls = scrapy.Field()
    created_time = scrapy.Field()
    updated_time = scrapy.Field()
    voteup_count = scrapy.Field()
    comment_count = scrapy.Field()
    author_name = scrapy.Field()
    author_url_token = scrapy.Field()
    author_headline = scrapy.Field()
    author_gender = scrapy.Field()


# 1.连接数据库，传入必要参数数据库地址，用户名，密码，数据库名
db = peewee.MySQLDatabase('liu', **{'host': '127.0.0.1',
                                         'password': '123456',
                                         'port': 3307,
                                         'user': 'root'})



class ZhihuAnswerEntity(peewee.Model):
    id = peewee.IntegerField()
    content = peewee.CharField(max_length=5000)
    created_time = peewee.BigIntegerField(verbose_name='创建时间', null=False, default=0)
    updated_time = peewee.BigIntegerField(verbose_name='修改时间', null=False, default=0)
    voteup_count = peewee.IntegerField(verbose_name='赞同数', null=False, default=0)
    comment_count = peewee.IntegerField(verbose_name='评论数', null=False, default=0)
    author_name = peewee.CharField(max_length=100)
    author_url_token = peewee.CharField(max_length=200)
    author_headline = peewee.CharField(max_length=1000)
    author_gender = peewee.IntegerField(verbose_name='性别', default=-2)


    class Meta:
        database = db
        db_table = 'gz_zobz'


if __name__ == '__main__':
    ZhihuAnswerEntity.create_table()
    # entity = ZhihuAnswerEntity.create(id=100, content='abc', image_urls='urls')
    # entity.save()
