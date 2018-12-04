# -*- coding: utf-8 -*-
# @Project : MovieWordCloud 
# @Time    : 2018/11/29 12:50
# @Author  : zsr
# @File    : Paths.py
# @Software: PyCharm
import time
import os

base_path=os.path.dirname(__file__)

COMMENTS_DIR=os.path.join(base_path,'douban',time.strftime('%Y%m%d',time.localtime()))

CONFIGER_PATH=os.path.join(base_path,'config')

MOVIE_WEEK_PATH=os.path.join(base_path, 'movieweek')
if not os.path.exists(MOVIE_WEEK_PATH):
    os.makedirs(MOVIE_WEEK_PATH)
