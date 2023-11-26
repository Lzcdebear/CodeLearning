# 读取 lrc 文件，处理歌词并保存到 lyc.txt 文件
"""
读取txt文件
时间戳为 [] 内容，删除
将文件之间的换行换为 ,
保存到output文件的最后一行
"""
import os


def process_lrc(input_num):
    filepath = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(filepath, 'lyric', str(input_num)+'.txt'), 'r', encoding='utf-8') as f1:
        lines = f1.readlines()
        lyrics = []
        for line in lines:
            # 找到歌词内容
            start_idx = line.find('[')
            end_idx = line.find(']')
            if start_idx != -1 and end_idx != -1:
                lyric = line[end_idx + 1:].strip()
                lyrics.append(lyric)
        # 将歌词用空格连接
        processed_lyrics = ' '.join(lyrics)

        # 写入 lyc.txt 文件
        with open(os.path.join(filepath, 'lyric', 'lyc.txt'), 'a', encoding='utf-8') as f2:
            f2.write(processed_lyrics + '\n')
