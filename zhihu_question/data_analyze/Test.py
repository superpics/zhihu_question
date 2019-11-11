#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释
import json
import re
import urllib.parse




if __name__ == "__main__":
    for user_token in open('/Users/liu/Documents/zhihu/to_get_followee'):

        user_token_no_warp = user_token.replace('\n', '')
        if "\n" in user_token_no_warp:
            print("包含换行符")
        else:
            print("不包含换行符")






