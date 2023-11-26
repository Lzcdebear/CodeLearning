import pandas as pd


def process_csv(input_file, output_file):
    # 读取CSV文件
    df = pd.read_csv(input_file)

    # 删除空白行
    df = df.dropna()

    # 删除重复项
    df = df.drop_duplicates()

    # 将处理后的数据写回到新的CSV文件
    df.to_csv(output_file, index=False)


# 调用函数，替换 'input.csv' 和 'output.csv' 为你的实际文件名
filename = input("Enter Name")
process_csv(filename+'.csv', filename+'_pure.csv')
