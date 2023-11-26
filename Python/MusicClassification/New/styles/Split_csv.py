import os
import pandas as pd


def split_csv(input_filename):
    # 读取原始CSV文件
    df = pd.read_csv(input_filename)

    # 拆分为每8行一个新文件
    rows_per_file = 5
    total_rows = df.shape[0]
    num_files = (total_rows + rows_per_file - 1) // rows_per_file

    for i in range(num_files):
        start_idx = i * rows_per_file
        end_idx = min((i + 1) * rows_per_file, total_rows)

        # 获取拆分后的数据块
        subset_df = df.iloc[start_idx:end_idx]

        # 构建新文件名
        output_filename = f"{os.path.splitext(input_filename)[0]}_{i + 1}.csv"

        # 将数据块保存为新的CSV文件
        subset_df.to_csv(output_filename, index=False)

        print(f"拆分后的文件 {output_filename} 保存成功！")


# 示例用法
name = input("enter word")
input_csv_filename = name + ".csv"  # 替换成你的CSV文件路径
split_csv(input_csv_filename)
