# -*- coding: utf-8 -*-
# @Project : MovieWordCloud 
# @Time    : 2018/11/28 17:40
# @Author  : zsr
# @File    : get_movies.py
# @Software: PyCharm

from requests_html import HTMLSession
import os
def get_movies():
    se=HTMLSession()
    douban_movie='https://movie.douban.com/'
    r=se.get(douban_movie)
    now_playings=r.html.find('#screening > div.screening-bd > ul')[0]
    movies=now_playings.find('li[class^=ui-slide-item]')
    i=1
    MOVIES={}
    for m in movies:
        print(i)
        try:
            movie_name=m.attrs['data-title']
            movie_url=m.attrs['data-trailer']
            movie_home=os.path.dirname(movie_url)
            movie_id=os.path.basename(movie_home)
            MOVIES[movie_id]=('{}、{}'.format(i,movie_name),movie_home)
        except Exception as e:
            print(e)
            pass
        i+=1
    se.close()
    return MOVIES