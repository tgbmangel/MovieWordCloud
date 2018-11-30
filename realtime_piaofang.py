# -*- coding: utf-8 -*-
# @Project : MovieWordCloud 
# @Time    : 2018/11/30 17:32
# @Author  : zsr
# @File    : realtime_piaofang.py
# @Software: PyCharm
import requests
import datetime
url='http://www.cbooo.cn/BoxOffice/GetHourBoxOffice'

#周票房
week_url='http://www.cbooo.cn/BoxOffice/getWeekInfoData?sdate={}-{}-{}'
a=datetime.datetime.now()
t_start=datetime.date(2018, 11, 19)
t_end = t_start + datetime.timedelta(days=6)
print('周期: {} 到 {}'.format(t_start, t_end))
# if t.isocalendar()[2]==1:
#     week_url=week_url.format(t.year,t.month,t.day)
#     resp=requests.get(week_url)
#     print(resp.json())
#
# rsp=requests.get(url)
# print(rsp.json())
