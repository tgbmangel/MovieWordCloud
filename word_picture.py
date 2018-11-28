# -*- coding: utf-8 -*-
# @Project : P3 
# @Time    : 2018/11/28 9:17
# @Author  : zsr
# @File    : word_picture.py
# @Software: PyCharm
from matplotlib import pyplot as plt
from collections import Counter
from wordcloud import WordCloud
import jieba
import jieba.posseg as psg
import numpy
from PIL import Image
import os

class MovieCloudWord(object):
    '''通过评论的txt文档来分词，然后做成词云图'''
    def __init__(self,movie_id,pic=None):
        self.movie_id=movie_id
        self.text_path='douban_comments/{}/{}.txt'.format(self.movie_id,self.movie_id)
        self.stopword_file='config/stopwords.txt'
        self.user_dict='config/{}/user_dict.txt'.format(self.movie_id)
        self.cloud_word_path = 'douban_comments/{}/{}.png'.format(self.movie_id, self.movie_id)
        self.stop_words = {}
        self.word_dict = {}
        self.picture_path = pic
        self.font = r'C:\Windows\Fonts\FZSTK.TTF'
    @property
    def get_stopwords(self):
        '''
        读取停用词
        :return:
        '''
        print('读取停用词库')
        with open(self.stopword_file, 'r', encoding='utf-8') as f:
            line = f.readline().rstrip('\n')
            while line:
                self.stop_words[line] = 1
                line = f.readline().rstrip('\n')
        print(self.stop_words)
        return self.stop_words

    def file_exists(self,filename):
        if os.path.exists(filename):
            return filename
        else:
            return
    @property
    def get_word_frequence(self):
        print('使用jieba分词中......')
        with open(self.text_path, 'r', encoding='utf-8') as f:
            get_text = ' '.join([x.strip() for x in f.readlines()])
            stopwords_get = self.get_stopwords
            _user_dic = self.file_exists(self.user_dict)
            if _user_dic:
                jieba.load_userdict(_user_dic)
            filter_key = ('a', 'n', 'e', 'o')
            seg = [x.word for x in psg.cut(get_text) if x.flag.startswith(filter_key)]
            c = Counter([x for x in seg if len(x) > 1 and not x.isdigit()]).most_common(100)
            for k, v in c:
                if k in stopwords_get:
                    pass
                else:
                    self.word_dict[k] = v
            print(self.word_dict)
            return self.word_dict

    def generate_wc(self):
        '''生成词云图'''
        if self.picture_path:
            _picture_mask = numpy.array(Image.open(self.picture_path))
            _wc = WordCloud(font_path=self.font,
                           background_color='white',
                           width=1000,
                           height=800,
                           mask=_picture_mask
                           )
        else:
            _wc = WordCloud(font_path=self.font,
                           background_color='white',
                           width=1000,
                           height=800,
                           )
        _wc.generate_from_frequencies(self.get_word_frequence)
        _wc.to_file(self.cloud_word_path)

if __name__=='__main__':
    moive = '27073234'
    pic_mask= 'imgs/bg.jpg'
    a = MovieCloudWord(moive, pic=pic_mask)
    a.generate_wc()