# -*- coding: utf-8 -*-
# @Project : P3 
# @Time    : 2018/11/28 15:41
# @Author  : zsr
# @File    : main.py
# @Software: PyCharm
from get_words import DoubanMovieComments
from word_picture import MovieCloudWord

if __name__=="__main__":
    moive = '26147417'
    mv = DoubanMovieComments(moive)
    mv.get_comments()
    mv.tear_down()
    a = MovieCloudWord(moive)
    a.generate_wc()