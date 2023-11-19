from Songs import Songs,Playlists
from Setting import Settings
import Web as wb
from wordedit import WordEdit

import os
st = Settings
file_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(file_dir, 'saves', self.keyword + '_build_list.csv')


def search_and_save():
    pls = Playlists(keyowrd=st.search_keyword,
                    limit=st.result_limit)
    # 获取前50的歌单
    pls.get_playlist()
    # 递归下载歌单
    pls.recur_playlists()
    if not os.path.exists(os.path.join(file_dir,'saves',st.f_csv_name,'_with_lyrics.csv')):
        pls.get_lyric()


def single_playlist():
    if not os.path.exists(os.path.join(file_dir,'saves',st.f_csv_name,'.csv')):
        # 创建一个新的歌单
        s = Songs(keyword=st.search_keyword,
                  limit=st.result_limit)
        s.get_plist_songs(st.playlist_url)
        s.get_lyric()

if __name__=="__main__":
    if st.toggle:
        search_and_save()
    else:
        single_playlist()
    w = WordEdit()
    w.get_wordpool()
    if st.word_rank:
        w.word_freq()
    w.get_wordpool()
