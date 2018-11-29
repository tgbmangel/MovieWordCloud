# -*- coding: utf-8 -*-
# @Project : P3 
# @Time    : 2018/11/28 13:42
# @Author  : zsr
# @File    : get_words.py
# @Software: PyCharm

from requests_html import HTMLSession
import time
import os
from Paths import COMMENTS_DIR

class DoubanMovieComments(object):
    '''从豆瓣获取电影评论（200条热评）'''
    def __init__(self,movie_name,movie_id):
        self.se=HTMLSession()
        self.movie_id=movie_id
        self.movie_name=movie_name
        self.moive_comment_path=os.path.join(COMMENTS_DIR, movie_name[:6] + movie_id)
        self.base_url='https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score&status=P'
        self.douban_comments_all = os.path.join(self.moive_comment_path, f'{movie_id}_all.txt')
        self.douban_comments = os.path.join(self.moive_comment_path, f'{movie_id}.txt')
        self.douban_movie_info =os.path.join(self.moive_comment_path, 'movieinfo.txt')
        self.STARS,self.STAR_MAN=0,0
        if not os.path.exists(os.path.dirname(self.douban_comments_all)):
            os.makedirs(os.path.dirname(self.douban_comments_all))

    def get_comments(self):
        self.f = open(self.douban_comments_all, 'wt', encoding='utf8')
        self.f1 = open(self.douban_comments, 'wt', encoding='utf8')
        page = 1
        do = True
        with open(self.douban_movie_info, 'wt', encoding='utf8') as f2:
            print(f'{self.movie_name}\n{self.movie_id}',file=f2)
        while do:
            print(page)
            _url = self.base_url.format(self.movie_id, (page - 1) * 20)
            try:
                print(_url)
                r = self.se.get(_url)
                divs = r.html.find('#comments > div.comment-item')
                print(f'找到记录：{len(divs)}条')
                if len(divs) == 0:
                    do = False
                    print('当前页没找到任何东西')
                for div in divs:
                    # print('='*10)
                    votes = div.find('div.comment > h3 > span.comment-vote > span.votes')[0].text
                    user_name = div.find('div.comment > h3 > span.comment-info > a')[0].text
                    try:
                        stars_div=div.find('div.comment > h3 > span.comment-info > span[class^=allstar]')[0]
                        stars = stars_div.attrs['class'][0][-2:-1]
                        self.STARS=self.STARS+int(stars)
                        self.STAR_MAN+=1
                    except IndexError:
                        stars = '-'
                        print('没评星')

                    p_time = div.find('div.comment > h3 > span.comment-info > span.comment-time')[0].text
                    p_text = div.find('div.comment > p')[0].text
                    comments = f'用户：{user_name}\n时间：{p_time}\n推荐：{stars}星\n同意数：{votes}\n{p_text}\n'
                    print(comments, file=self.f)
                    print(p_text, end='\n', file=self.f1)
                    # print('=' * 10)
                page += 1
                time.sleep(1)
            except Exception as e:
                print(e)
                print(page)
                do = False
    def tear_down(self):
        self.f.close()
        self.f1.close()
        self.se.close()

if __name__=="__main__":
    movie_name='ss'
    moive = '27102739'
    mv = DoubanMovieComments(movie_name,moive)
    mv.get_comments()
    mv.tear_down()
    print('人均推荐：{:.2f}'.format(mv.STARS/mv.STAR_MAN))