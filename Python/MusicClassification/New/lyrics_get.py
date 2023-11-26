import requests
import json
from selenium import webdriver
import os
import csv
import time
from txt_lyric import process_lrc

def read_cookie():
    try:
        print("[INFO]:正常尝试读取本地cookie")
        with open('wyycookie.txt', 'r', encoding='utf8') as f:
            Cookies = f.read()
            # print(Cookies)
    except:
        print("[ERROR]:读取失败，请手动登录并更新")
        get_cookies()
        read_cookie()
    return Cookies
def get_cookies():
    driver = webdriver.Firefox()
    url = 'https://music.163.com/'
    driver.get(url)  # 发送请求
    # 打开之后，手动登录一次
    time.sleep(3)
    input('完成登陆后点击enter:')
    time.sleep(3)
    dictcookies = driver.get_cookies()  # 获取cookies
    cookie = [item["name"] + "=" + item["value"] for item in dictcookies]
    cookiestr = ';'.join(item for item in cookie)
    print(cookiestr)
    with open('wyycookie.txt', 'w') as f:
        f.write(cookiestr)
    print('cookies保存成功！')
    driver.close()
rs = requests.session()
def get_ID(name):
    url = 'https://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={' + str(
        name) + '}&type=1&offset=0&total=true&limit=1'
    r = rs.get(url, headers=headers)
    r.encoding = 'utf-8'
    str_r = r.text
    dict_r = json.loads(str_r)
    # print(dict_r)
    # print(dict_r["result"]['songs'][0]['id'])
    ID = dict_r["result"]['songs'][0]['id']
    return ID
def get_poem(name, id):
    url = 'https://music.163.com/api/song/lyric?id={}&lv=1&kv=1&tv=-1'.format(id)
    r = rs.get(url, headers=headers)
    r.encoding = 'utf-8'
    str_r = r.text
    dict_r = json.loads(str_r)
    lyric = dict_r.get('lrc', {}).get('lyric', '')
    if lyric:
        # 将歌词保存到文件
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lyric', str(name) + '.txt')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(lyric)
        print(f'歌词保存成功！保存路径: {file_path}')
    else:
        print('未找到歌词信息。')
def get_songlist(style):
    try:
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'styles', style + '.csv')
        # 打开CSV文件并读取内容
        with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            # 将每一行的两列内容合并到一个列表中
            merged_lines = [','.join(row) for row in csv_reader]
        return merged_lines

    except FileNotFoundError:
        print(f"文件 {file_path} 不存在.")
        return []

    except Exception as e:
        print(f"发生异常: {e}")
        return []


Cookies = read_cookie()
headers = {
    'Referer': 'http://music.163.com',
    'Host': 'music.163.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Cookie': '{}'.format(Cookies)}

style = "流行_pure"  # 在这里填入曲风类型
num_style = 6  # 在这里填入需要的曲风歌曲表编号，从 1 开始
m = 26  # 在这里编辑输出歌曲的编号

style_re = style+"_"+str(num_style)
# 获取歌曲名字
song_list = get_songlist(style_re)
# 每个歌单有多少歌
length = len(song_list)
for j in range(1, length):
    name = song_list[j]
    id = get_ID(name)
    print(id)
    get_poem(m, id)
    print("=" * 500)
    time.sleep(2)
    m += 1
    process_lrc(j)
print("请将程序内的 m 的值改为 "+str(m)+" 然后更改 num_style 值的大小、style 的曲风类型后重新运行")