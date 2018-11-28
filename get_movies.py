# -*- coding: utf-8 -*-
# @Project : MovieWordCloud 
# @Time    : 2018/11/28 17:40
# @Author  : zsr
# @File    : get_movies.py
# @Software: PyCharm

from requests_html import HTMLSession
se=HTMLSession()
douban_movie='https://movie.douban.com/'
r=se.get(douban_movie)
now_playings=r.html.find('#screening > div.screening-bd > ul')[0]
movies=now_playings.find('li[class^=ui-slide-item]')
i=0
for m in movies:
    print(i)
    print(m.attrs['data-title'])
    print(m.attrs['data-trailer'])
    i+=1