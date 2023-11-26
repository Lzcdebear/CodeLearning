import os

file_dir = os.path.dirname(os.path.abspath(__file__))
# 将路径设置为该python同一路径下的文件夹saves内的csv文件
filepath = os.path.join(file_dir, 'saves', '_build_list.csv')
print(filepath)
print(file_dir)