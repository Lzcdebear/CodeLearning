import csv
import pandas as pd

def txt_to_csv(txt_filename, csv_filename):
    # 打开txt文件并读取内容
    with open(txt_filename, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()

    # 分割每行的内容并写入CSV文件
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        # 分割每行的内容并写入CSV文件
        for line in lines:
            # 使用" - "分隔两列，并去除两侧的空格
            columns = [col.strip() for col in line.split(" - ")]

            # 写入CSV文件，只保留第一列
            csv_writer.writerow([columns[0]])





# 使用示例
input_name = input("输入txt文件名称")
txt_to_csv(input_name + ".txt", input_name + '.csv')
