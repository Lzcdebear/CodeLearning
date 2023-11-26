import pandas as pd
import os
import re
import pkuseg
from collections import Counter

filepath = os.path.dirname(os.path.realpath(__file__))


# 这个函数需要输入曲风，然后在lyric中找到 曲风.txt 然后和 保存到data下的 data.csv
# 第一列为曲风，第二列为歌词
def get_lyric_csv(genre):
    # 读取txt文件
    filepath = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(filepath, 'lyric', genre + '.txt'), 'r', encoding='utf-8') as file:
        txt_lines = file.readlines()

    # 创建一个DataFrame，将歌词存储到其中，第一列为曲风（命名为'a'），第二列为歌词，不添加索引
    txtdata = pd.DataFrame([[genre] * len(txt_lines), txt_lines]).T
    # 去除txtdata中的NaN
    txtdata = txtdata.dropna()

    # 输出DataFrame
    print("这里是txtdata===================================================================")
    print(txtdata)

    if os.path.getsize(os.path.join(filepath, 'data', 'data.csv')) > 0:
        # 读取 CSV 文件，不指定列名
        csvdata = pd.read_csv(os.path.join(filepath, 'data', 'data.csv'), header=None)
        # 检查 DataFrame 是否为空
        if not csvdata.empty:
            # 重置索引为默认排序（0开始）
            csvdata.reset_index(drop=True, inplace=True)
            # 输出合并后的DataFrame
            print("这里是csvdata===================================================================")
            print(csvdata)
        else:
            print("CSV 文件中没有数据.")
    else:
        # 如果文件为空，创建一个空白 DataFrame
        csvdata = pd.DataFrame(columns=[])
    # 输出合并后的DataFrame
    print("这里是csvdata===================================================================")
    print(csvdata)

    # 将txtdata合并到csvdata后面
    merged_data = pd.concat([csvdata, txtdata], axis=0, ignore_index=True)

    # 输出合并后的DataFrame
    print("这里是mearged_data===================================================================")
    print(merged_data)
    # 将合并后的DataFrame保存为CSV文件，覆盖原有文件
    merged_data.to_csv(os.path.join(filepath, 'data', 'data.csv'), index=False)


def word_purify():
    filepath = os.path.dirname(os.path.realpath(__file__))
    # 读取csv文件，csv第一列为曲风，第二列为歌词
    ori_data = pd.read_csv(os.path.join(filepath, 'data', 'data.csv'))
    # 读取第二列歌词，保存为字符串
    lyrics_column = ori_data.iloc[:, 1].astype(str)
    # 去除其中的特殊符号和英文，仅保留中文字符
    lyrics_column = lyrics_column.apply(lambda x: re.sub(r'[^\u4e00-\u9fa5]+', '', x))
    # 将处理后的字符串重新赋给ori_data
    ori_data.iloc[:, 1] = lyrics_column
    # 输出处理后的DataFrame
    print(ori_data)
    # 将处理后的DataFrame保存到CSV文件
    ori_data.to_csv(os.path.join(filepath, 'data', 'data.csv'), index=False)


def word_freq():
    filepath = os.path.dirname(os.path.realpath(__file__))
    oridata = pd.read_csv(os.path.join(filepath, 'data', 'data.csv'))

    # 初始化pkuseg分词器
    seg = pkuseg.pkuseg()
    # 创建新的DataFrame
    new_dataframe = pd.DataFrame(columns=['0', '1'])

    # 循环处理每一行的歌词
    for index, row in oridata.iterrows():
        lyrics = str(row['1'])
        # 使用pkuseg进行分词
        words = seg.cut(lyrics)
        # 统计词语出现的次数
        word_counts = Counter(words)
        # 对出现次数从高到低进行排序，取前20
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:20]
        # 添加到新的DataFrame中
        new_dataframe = new_dataframe.append({'0': row['0'], '1': sorted_word_counts},
                                             ignore_index=True)
    # 输出新的DataFrame
    print(new_dataframe)
    # 保存新的DataFrame到CSV文件
    # 判断输出的CSV文件是否存在
    output_csv_file = os.path.join(filepath, 'data', 'word_freq.csv')
    if os.path.exists(output_csv_file):
        # 如果文件存在，追加保存
        new_dataframe.to_csv(output_csv_file, mode='a', header=False, index=False)
    else:
        # 如果文件不存在，创建新文件
        new_dataframe.to_csv(output_csv_file, index=False)


# while True:
#     i = input("Enter Word")
#     get_lyric_csv(i)
