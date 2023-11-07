class Settings:
    # 是否爬取整个歌单
    toggle = False
    # 设置搜索的关键词
    search_keyword = ''
    # 设置结果的限制数量
    result_limit = 20
    
    # 设置歌单的url，对于仅爬取一张歌单的时候
    playlist_url = 'https://music.163.com/#/discover/toplist?id=3778678'
    playlist_title = '云音乐热歌榜'
    # 设置分词过滤器强度
    filter_setting = 'm'
    '''
    空格 为没有
    m 为去语气
    e 为去英文语气
    '''
    # 打印排名
    word_rank = True
    num = 50
    f_csv_name = search_keyword if toggle else playlist_title
    
    # 初始化函数
    def __init__(self):
        pass
    
    '''将搜索词给到Settings类并存储'''
    def set_search_word_for_list(self, search_word):
        self.search_keyword = search_word
        self.toggle = True
        self.f_csv_name = search_word
