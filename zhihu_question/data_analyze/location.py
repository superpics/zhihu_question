#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释
import re

from zhihu_question.items import ZhihuAnswerEntity
from cocoNLP.extractor import extractor

if __name__ == '__main__':
    query_result = ZhihuAnswerEntity.select(ZhihuAnswerEntity.author_url_token, ZhihuAnswerEntity.content).where(ZhihuAnswerEntity.question_id == 311464426).limit(100)
    ex = extractor()
    for entity in query_result:
        # print(entity.content)
        # print(ex.extract_locations(entity.content))
        # print('-'*40)

        search = re.search(r'(男|女|女孩|男孩|独子|独女|妹子|汉子|女汉子|汉纸|妹纸|女汉纸|姑娘)', entity.content, flags=0)
        if search:
            print(search.group(1) + "|||||" + entity.content)
        else:
            print("空" + "|||||" + entity.content)