# -*- coding: utf-8 -*-
# @Project : P3 
# @Time    : 2018/11/28 15:41
# @Author  : zsr
# @File    : main.py
# @Software: PyCharm
from get_movies import get_movies
from get_words import DoubanMovieComments
from word_picture import MovieCloudWord

if __name__=="__main__":
    movies=get_movies()
    pic_mask = 'imgs/bg.jpg'
    for moive_id, (movie_name,movie_url) in movies.items():
        print(moive_id)
        mv = DoubanMovieComments(movie_name,moive_id)
        mv.get_comments()
        mv.tear_down()
        if mv.STAR_MAN:
            mv_score=mv.STARS/mv.STAR_MAN
        else:
            mv_score=0.0
        a = MovieCloudWord(movie_name,moive_id,pic=pic_mask)
        a.generate_wc()
        a.write_shuiyin(movie_name,mv_score)