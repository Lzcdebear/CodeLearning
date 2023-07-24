# 实验一
# （1）导入库
import numpy as np
from sklearn.cluster import KMeans  #导入KMeans类
from matplotlib import pyplot as plt
# （2）随机生成500个数据（每个数为0-1间的浮点数）
X = np.random.rand(500,3)  # 生成一个随机数组，shape为500*3（样本大小为500, 特征数为3）
# （3）利用散点图将数据展示出来
plt.figure(figsize=(16, 10), dpi=144)
plt.scatter(X[:, 0], X[:, 1], s=200, cmap='cool') #将样本的前2个属性与坐标轴x、y对应，画出散点图
plt.show()
# （4）使用KMeans模型拟合，聚类数设为2。
kmean = KMeans(n_clusters=2)  #生成KMeans模型实例，聚类数设为2
kmean.fit(X)   #训练模型
# （5）将聚类结果利用散点图显示出来
labels = kmean.labels_  #获取数据点的类别标签
centers = kmean.cluster_centers_  #获取质心的坐标
fig = plt.figure(figsize=(8, 5), dpi=144)
plt.scatter(X[:,0], X[:,1], c=labels, edgecolor='k')  #用散点图绘出数据点前2属性对应的坐标，用不同颜色显示聚类结果
plt.scatter(centers[:,0], centers[:,1], s=50, marker="*")  # 显示质心
plt.show()