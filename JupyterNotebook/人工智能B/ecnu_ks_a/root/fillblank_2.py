# fillblank_2.py

# 导入库
import matplotlib.pyplot as plt
from ________【1】________ import KMeans # 导入聚类库
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False

# 加载数据集并提取数据
data_ori = ________【2】________  # 读取housing.csv数据
data = ________【3】________ # 提取聚类需要使用的三列元素

# 从键盘输入聚类数
n = int(input("请输入聚类数：\n"))

# 聚类训练
res = KMeans(________【4】________, random_state = 1)  # 设置聚类数为n
res.fit(data)

# 展示结果
labels = res.labels_ 
centers = ________【5】________  # 设置所有质心
print(centers)