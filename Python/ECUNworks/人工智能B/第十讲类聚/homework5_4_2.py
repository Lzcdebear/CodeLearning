# 实验2
# （1）导入库
import numpy as np
from sklearn.cluster import KMeans  #导入KMeans类
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs

# （2）利用make_blobs函数生成200个样本数据，特征数为2的数据
x, y = make_blobs(n_samples=200, n_features=2)
print(x)
print(y)
# （3）利用散点图展示出来
plt.figure(figsize=(6, 4), dpi=144)
plt.xticks(())
plt.yticks(())
plt.scatter(x[:,0], x[:,1], s=20, marker='o')  #将样本的前2个属性与坐标轴x、y对应，画出散点图
plt.show()
# （4）利用Kmeans函数聚类，聚类簇设为4
n_clusters = 4
kmean = KMeans(n_clusters)  #生成KMeans模型实例，聚类数设4
kmean.fit(x)  #训练模型
# （5）将结果利用散点图显示出来
labels = kmean.labels_  #获取数据点的类别标签
centers = kmean.cluster_centers_  #获取质心的坐标

markers = ['o', '^', '*', 'D']
colors = ['r', 'b', 'y', 'g']
plt.figure(figsize=(6, 4), dpi=144)
plt.xticks(())
plt.yticks(())
for c in range(n_clusters):
    cluster = x[labels == c]   #cluster为数据集中某一类标签的数据
    plt.scatter(cluster[:, 0], cluster[:, 1], marker=markers[c], s=20, c=colors[c]) #用不同标记和不同颜色标记不同类的数据
plt.scatter(centers[:, 0], centers[:, 1], marker='o', c="white", alpha=0.9, s=300)  #用白色圆圈画出质心
for i, c in enumerate(centers):
    plt.scatter(c[0], c[1], marker='$%d$' % i, s=50, c=colors[i]) #在质心位置标上类别的数字
plt.show()