#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释
import re

from cocoNLP.extractor import extractor

from zhihu_question.items import ZhihuAnswerEntity

# .where(ZhihuAnswerEntity.question_id == 311464426).limit(500)
query_result = ZhihuAnswerEntity.select(ZhihuAnswerEntity.author_url_token, ZhihuAnswerEntity.content, ZhihuAnswerEntity.author_gender, ZhihuAnswerEntity.author_name)
ex = extractor()


def tall_self():
    # 13x、14x、15x、16x、17x、18x、19x、1米3、1米4、1米5、1米6、1米7、1米8、1米9
    exp = r'(1[456789]\dcm|1[456789]\d|1米\d)\D'
    for entity in query_result:
        search = re.search(exp, entity.content, flags=0)
        if search:
            tall = search.group(1).replace("1米9", "190")\
                .replace("1米8", "180") \
                .replace("1米7", "170")\
                .replace("1米6", "160")\
                .replace("1米5", "150")\
                .replace("cm", "")
            print(int(int(tall) / 5) * 5)
            # print(entity.content)
            # print("==========")
        else:
            print("-1")
            # print("==========")


def old_self():
    exp = r'([23]\d岁|2\d|3\d)'
    for entity in query_result:
        search = re.search(exp, entity.content, flags=0)
        if search:
            print(search.group(1) + "="*5 + entity.content)
        else:
            print("-1" + "="*5 + entity.content)

def born_self():
    born_exp = r'\D(19[789]\d|9\d|8\d)\D'
    old_exp = r'\D([23]\d岁|2\d|3\d)\D'
    for entity in query_result:
        content_deal = entity.content.replace("80后", "").replace("90后", "")
        born_search = re.search(born_exp, content_deal, flags=0)
        if born_search:
            to_deal = born_search.group(1)
            if len(to_deal) == 2:
                to_deal = "19" + to_deal
            print(to_deal)
            # print(content_deal)
            # print("===")
        else:
            search = re.search(old_exp, entity.content, flags=0)
            if search:
                to_deal = int(search.group(1).replace('岁', ''))
                full_old = -1
                if 0 < to_deal < 50:
                    full_old = 2019 - to_deal
                print(str(full_old))
            else:
                print("-1")


if __name__ == '__main__':
    # old_self()
    born_self()
    # tall_self()



