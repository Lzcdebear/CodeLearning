# fillblank_2

# 导入库
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans # 导入聚类库
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False

# 加载数据集并提取数据
data_ori = pd.read_csv('F:\\OneDrive\\Coding\\Python\\ECUNworks\\人工智能B\\ecnu_ks_a\\root\\housing.csv') # 读取housing.csv数据
data = data_ori.loc[:,['longitude','latitude','median_income']]  # 提取聚类需要使用的三列元素

# 从键盘输入聚类数
n = int(input("请输入聚类数：\n"))

# 聚类训练
res = KMeans(n_clusters=n, random_state = 1)  # 设置聚类数为n
res.fit(data)

# 展示结果
labels = res.labels_ 
centers = res.cluster_centers_  # 设置所有质心
print(centers)