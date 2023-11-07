import time
import re
import json
import os
# 网页获取
from bs4 import BeautifulSoup
import pandas as pd
# 自己写的Web文件和Setting文件
import Web as wb
from Setting import Settings as st

class Songs:
    def __init__(self,keyowrd,limit):
        self.only_lyric=[]
        self.plist = None
        self.keyword = keyowrd
        self.limit = limit
    
    '''获取歌单歌曲的id、name、url，并存储到Songs类中的plist中'''
    def get_playlist_song(self,url):
        if self.plist is None:
            self.plist = pd.DataFrame(columns=['id','name','url'])
        # 建立歌单的索引对象
        content = wb.get_web(url).text
        # 建立bs4对象
        bsoup = BeautifulSoup(content,'lxml')
        bsoup_plist = bsoup.find(name='ul',attrs={'class':'f-hide'})
        # 导入Setting中的对象的属性确定继续方案
        if not st.toggle:
            st.f_csv_name = st.playlist_title = bsoup.find(name='h2', class_='f-ff2').string
        # 筛选数据
        songs = {'id':[],'name':[],'url':[]}
        for song in bsoup_plist.find_all(name='li'):
            # id
            id = re.search('=([0-9])',song.a['href'])
            # 避免重复记录歌曲名字
            id_foo = id.group(1)
            if id_foo not in self.plist['id']:
                # 如果没有出现就加入到id中
                songs['id'].append(id_foo)
                # 如果id已经存入了则一定没有出现，这里再存储name
                song_name = song.a.string
                songs['name'].append(song_name)
                # 存储url
                song_url = 'https://music.163.com'+song.a['href']
                songs['url'].append(song_url)
                songs['lyric'] = ''
        df = pd.DataFrame(songs,columns=['id','name','url'])
        self.plist = self.plist.append(df,ignore_index=True)
    
    '''获取歌单中歌曲的歌词'''
    def get_lyric(self):
        # 读取该python文件的路径
        file_dir = os.path.dirname(os.path.abspath(__file__)) 
        # 将路径设置为该python同一路径下的文件夹saves内的csv文件
        filepath = os.path.join(file_dir, 'saves', self.keyword + '_build_list.csv')
        # 判断文件是否存在，不存在就报错
        if not os.path.exists(filepath):
            print('file not found')
            exit(-1)
        # plist中存储csv中出现的内容
        plist = pd.read_csv(filepath)
        plist = plist.drop('Unnamed:0',axis=1)
        plist_temp = pd.DataFrame(columns=plist.columns)
        total = len(plist['id'])
        n=0
        
        for index, row in plist.iterrows():
            url = 'http://music.163.com/api/song/lyric?os=pc&id=' + str(row['id']) + '&lv=-1&kv=-1&tv='
            # wb.get_web()函数封装了请求发送的逻辑
            # .json()方法实现了JSON到字典的自动解析。
            content = wb.get_web(url).json()
            if 'lrc' in content and 'nolyric' not in content and content['lrc'] is not None:
                lyric = content['lrc']['lyric']
                try:
                    # 使用了将文件中[xxx]这样的东西用空字符代替，也就是时间
                    # .代表所有类型
                    # *代表可以重复出现
                    # ？代表尽可能少的匹配，非贪婪方法，也就是只会传入数字
                    lyric = re.sub('\[.*?\]', '', lyric)
                    row['lyric'] = lyric
                    print('completed ' + str(round(index / total * 100, 2)) + '% ', end='')
                    print('added lyric id: ' + str(row['id']))
                    plist_temp = plist_temp.append(row, ignore_index=True)
                except:
                    continue
            n += 1
            if n==300:
                break
            plist = plist_temp.copy()
            plist.to_csv(file_dir+st.search_keyword+'_with_lyrics.csv',encoding='utf-8')


class Playlists(Songs):
    def __init__(self, keyowrd, limit):
        super().__init__(keyowrd=keyowrd, limit=limit)
        self.playlists = []
    
    '''获取播放列表'''
    def get_playlist(self):
        # 读取python文件所在的位置
        file_dir = os.path.dirname(os.path.abspath(__file__)) 
        # 如果json文件不存在，则创建文件f1作为json
        if not os.path.exists(file_dir+self.keyword+'.json'):
            url = 'http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={' \
                  + self.keyword + '}&type=1000&offset=0&order=hot&total=true&limit=' + str(self.limit)
            json_content = wb.get_web(url).json() 
            with open(os.path.join(file_dir, 'saves', self.keyword + '.json'),'w',encoding='utf-8') as f1:
                # json.dumps将python中字典转化为json文件
                text = json.dumps(json_content,ensure_ascii=False)
                f1.write(text)
        #如果json文件存在则直接使用该文件
        with open(os.path.join(file_dir, 'saves', self.keyword + '.json'),encoding='utf-8') as f2:
            p_json = json.load(f2)
        result = p_json['resulr']
        self.playlists = result['playlists']
        return self.playlists
    
    '''重新处理播放列表'''
    def recur_playlists(self):
        """递归补充歌单列表、歌曲信息"""
        file_dir = os.path.dirname(os.path.abspath(__file__)) 
        os.path.join(file_dir, 'saves', self.keyword + '.json')
        if not os.path.exists(os.path.join(file_dir, 'saves', self.keyword + '-build-list.csv')):
            time.sleep(2)
            self.plist = pd.DataFrame(columns=['id', 'name', 'url'])
            for playlist in self.playlists:
                url = 'https://music.163.com/#/playlist?id=' + str(playlist['id'])
                self.get_playlist_song(url)
                print('completed ' + str(self.playlists.index(playlist) / len(self.playlists) * 100) + '%')
            self.plist.to_csv(file_dir + self.keyword + '-build-list.csv', encoding='UTF-8')
