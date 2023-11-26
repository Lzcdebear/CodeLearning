import os

filepath = os.path.dirname(os.path.realpath(__file__))
# 指定文件夹路径
folder_path = filepath

# 创建文件夹
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 生成1-70个txt文件
for i in range(1, 71):
    # 构造文件名
    filename = f'{i}.txt'
    # 构造文件路径
    file_path = os.path.join(folder_path, filename)

    # 创建空白文件
    with open(file_path, 'w'):
        pass

print(f'成功生成1-70个txt文件，文件保存在{folder_path}文件夹中。')
