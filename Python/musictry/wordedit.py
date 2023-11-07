#pip install wordcloud pkuseg matplotlib tabulate
from wordcloud import WordCloud  # 词云
import pkuseg  # pkuseg
from matplotlib import pyplot as plt  # 数据可视化库
import re
import pandas as pd
import time
import Web as wb
from collections import Counter
from Setting import Settings as st
import os

class WordEdit:
    def __init__(self):
        self.word_pool = []
        self.new_word_pool = []
        self.new_postag_pool = []
        self.len = None
        self.freq = {}
        self.setting = st
        self.file_dir = os.path.dirname(os.path.abspath(__file__)) 
        
    def get_wordpool(self):
        time_start = time.time()
        seg = pkuseg.pkuseg(postag=True)
        print('start processing')
        """获得分词组"""
        with open(os.path.join(self.file_dir, 'saves', self.setting.f_csv_name + '_with_lyrics.csv'), encoding='UTF-8') as p:
            songs = pd.read_csv(p)
            songs_temp = pd.DataFrame(columns=songs.columns)
            for index, row in songs.iterrows():
                # print(row['song_name'])
                if wb.chinese_contain(row['name']):
                    # make sure song tile contains chinese character, as a way to exclude
                    # English songs.
                    songs_temp = songs_temp.append(row)
            songs = songs_temp.copy()
            text = songs['lyric'].tolist()
            text_temp = []
            for lyric in text:
                if type(lyric) is not float:
                    text_temp.append(lyric)
            text = text_temp
            self.len = len(text)
            output = 'You have ' + str(self.len) + ' songs'
            print(output)
            with open(os.path.join(self.file_dir, 'saves', st.search_keyword + '_record.txt') ,'w',encoding='UTF-8') as rc:
                rc.write(output)
            lyrics = None
            try:
                lyrics = ' '.join(text)
            except Exception as ex:
                print(ex)
                print(text)
                exit(-1)
        reg = re.compile('\\n|/|-+|～+|&|\*+')
        lyrics = re.sub(reg, ' ', lyrics)
        self.word_pool = seg.cut(lyrics)
        self.filter_word(self.setting.filter_setting)
        time_end = time.time()
        print('time past: ', time_end - time_start, 's')
        
    def word_freq(self):
        print('start ranking')
        foo = []
        for word in self.new_word_pool:
            if len(word) >= 2:
                foo.append(word)
        freq = Counter(foo).most_common(len(self.new_word_pool))
        w, n = [],[]
        rg = min(self.setting.num,self.len)
        for i in range(rg):
            if i < (rg):
                w.append(freq[i][0])
                n.append(freq[i][1])
        for r in freq:
            self.freq[r[0]] = r[1]
        df = pd.DataFrame({'前1-'+str(rg): w, '次数': n}).set_index('前1-'+str(rg))
        df.to_csv(os.path.join(self.file_dir, 'saves', self.setting.search_keyword + '-word_rank.csv'), encoding='UTF-8')

    def filter_words(self, filter_setting = None):
        def make_filter(word_pool, stoplist):
            # 注意大小写不敏感
            new_word_pool = []
            new_postag_pool = []
            for word in word_pool:
                l_word = word[0].lower()
                if l_word not in stoplist:
                    new_word_pool.append(l_word)
                    new_postag_pool.append(word[1])
            return new_word_pool, new_postag_pool
        """修剪词语"""
        print('start filtering')
        useless = ['da', 'doo', 'ya', 'oh', 'ooh', 'la', 'ayy', 'woah', 'na', 'ah', 'nah',
                   'yeah','hey']
        with open(os.path.join(self.file_dir, 'saves', 'stoplist.txt'), encoding='UTF-8') as f:
            stoplist = f.read().splitlines()  # 不能用readlines(),因为会有换行符
        if filter_setting == 'm':
            sdf = stoplist+useless
            self.new_word_pool, self.new_postag_pool = make_filter(self.word_pool, sdf)
        elif filter_setting == 'e':
            with open(os.path.join(self.file_dir, 'saves', 'stoplist-e.txt'), encoding='UTF-8') as f:
                stopen = f.read().splitlines()
                eef = stoplist+stopen+useless
            self.new_word_pool, self.new_postag_pool = make_filter(self.word_pool, eef)
        else:
            self.new_word_pool, self.new_postag_pool = make_filter(self.word_pool, stoplist)
        return self.new_word_pool, self.new_postag_pool
    
    
    
    