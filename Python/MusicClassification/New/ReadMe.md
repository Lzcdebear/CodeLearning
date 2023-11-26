# 运行环境和需要
文件运行环境是 python 3.11 版本。使用的环境是 pycharm 2023.2.5。
文件需要的库安装

<big>**pip install pandas numpy scikit-learn selenium pkuseg**</big>

以下是文件具体使用方法

在网易云网页版查找到目标歌单进入歌单界面后复制网址到

https://yyrcd.com/n2s/ 

再在网页上读取歌单内容获取歌名和作者

# 获取歌词信息
将获得的文字内容保存到 **style** 文件下，创建一个txt文件保存。
之后运行 **TXT_to_CSV.py** ，获得csv文件，之后依次运行 **Purify_csv.py** 和
**Split_csv.py** 两个文件，获得没有重复歌名的歌曲信息文件。

# 获取歌曲歌词
在获取后运行 **lyrics_get.py** 文件获取歌词。注意，由于网易云限制，获取歌词的时候建议每次
获取都间隔10秒左右，保证获取不会被中断。
如果一切顺利，最终会在 **lyric** 文件夹下获得 **lyc.txt** 文件，将文件复制到同目录下，
并且改名为曲风名字，获得 **曲风.txt**。

# 处理实验数据获得数据内容
运行 **learning_get.py** 程序，将 **lyric** 下的歌词内容重新处理。

### 是否进行歌词文件转为csv操作
这部分将会把 **lyric** 下的txt文件转化为csv格式，并且保存在 **data** 文件夹下的 **data.csv**
文件中，保存方法为在最后添加，不改变原来内容，可以多次运行得到不容曲风的数据并保存到 **data.csv**
 文件中。

### 是否进行歌词整理和整合到data中的操作
只需要运行一次，将会把 **data** 文件夹下的 **data.csv** 文件读取并进行处理，最终得到每一首
歌歌词中词语的词频，这里使用的分词工具是 **_pkuseg_**。

# 机器学习
运行 **sklearning.py** 文件，开始机器学习，默认读取的文件为 
**_sklearning.py所在位置\\data\\word_freq.csv_**。 读取后开始机器学习。














