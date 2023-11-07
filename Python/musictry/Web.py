import requests
from requests.exceptions import RequestException
import re

'''获得网页内容'''
def get_web(url,params=None):
    #将链接内的/#改为空格
    url = re.sub('/#','',url)
    
    #设置网页的头文件
    web_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    
    #开始获取网页，总共尝试6次
    try_num = 6
    while try_num>0:
        try:
            response = requests.get(url,headers=web_headers,params=params)
            print(response.url)
            if response.status_code==200:
                web_headers=0
                return response
        except RequestException:
            try_num-=1
            print('retry now')
            if try_num<=0:
                return None
            
'''判断中文字符是否出现'''
def chinese_contain(check_str):
    try:
        for ch in check_str:
            if u'\u4e00'<=ch<=u'\u9fff':
                return True
        return False
    except:
        return False
