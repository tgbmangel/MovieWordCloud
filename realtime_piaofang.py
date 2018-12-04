# -*- coding: utf-8 -*-
# @Project : MovieWordCloud 
# @Time    : 2018/11/30 17:32
# @Author  : zsr
# @File    : realtime_piaofang.py
# @Software: PyCharm
import requests
import datetime
import os
from Paths import MOVIE_WEEK_PATH
url='http://www.cbooo.cn/BoxOffice/GetHourBoxOffice'

#上周票房
week_url='http://www.cbooo.cn/BoxOffice/getWeekInfoData?sdate={}-{}-{}'
t_now=datetime.datetime.now()
# t_start=datetime.date(2018, 11, 19)
t_start=t_now-datetime.timedelta(days=8)
t_end = t_start + datetime.timedelta(days=6)
print('周期: {} 到 {}'.format(t_start, t_end))
file_name=os.path.join(MOVIE_WEEK_PATH,'{}{}{}.txt'.format(t_start.year,t_start.month,t_start.day))
if t_start.isocalendar()[2]==1:
    try:
        if os.path.exists(file_name):
            print('已存在')
            pass
        else:
            week_url=week_url.format(t_start.year,t_start.month,t_start.day)
            resp=requests.get(week_url)
            print(resp.status_code)
            data1=resp.json().get('data1')
            data2=resp.json().get('data2')[0]
            if data1:
                print('找到数据')
                with open(file_name, 'wt', encoding='utf8') as f2:
                    print('统计周期：{}'.format(data2.get('sDate')),file=f2)
                    print('周总票房：{} 万'.format(data2.get('BoxOffice')),file=f2)
                    # print('以下是周榜TOP 10：',file=f2)
                    print('',file=f2)
                    for x in data1:
                        #排名
                        print('{}.《{}》'.format(x.get('MovieRank'),x.get('MovieName')),file=f2)
                        # 本周票房
                        print('本周票房：{} 万'.format(x.get('WeekAmount')),file=f2)
                        # 累计票房：
                        print('累计票房：{} 万'.format(x.get('SumWeekAmount')),file=f2)
                        #上映时长
                        print('上映时长：{} 天'.format(x.get('MovieDay')),file=f2)
                        print('',file=f2)
    except Exception as e:
        print(e)
# #
# rsp=requests.get(url)
# print(rsp.json())
