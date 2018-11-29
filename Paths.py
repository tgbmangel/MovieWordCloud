# -*- coding: utf-8 -*-
# @Project : MovieWordCloud 
# @Time    : 2018/11/29 12:50
# @Author  : zsr
# @File    : Paths.py
# @Software: PyCharm
import time
import os

base_path=os.path.dirname(__file__)
print(base_path)
COMMENTS_DIR=os.path.join(base_path,'douban',time.strftime('%Y%m%d',time.localtime()))
print(COMMENTS_DIR)
CONFIGER_PATH=os.path.join(base_path,'config')

