# 实验3
# （1）导入库
import numpy as np
from sklearn.cluster import KMeans  #导入KMeans类
from matplotlib import pyplot as plt
from sklearn import datasets
from mpl_toolkits.mplot3d import Axes3D  # 这个工具包可以显示 3D 图形
from sklearn.cluster import KMeans

plt.rcParams['font.sans-serif'] = ['SimHei']  # 避免中文出现乱码
plt.rcParams['axes.unicode_minus'] = False

# （2）利用load_iris()函数导入数据，并付给变量X
iris = datasets.load_iris()  # 导入iris数据
X = iris.data   #取属性集
# （3）设置变量存储类簇数，并分别进行Kmeans聚类，同时进行可视化
n_clusters_list = [2, 3, 4, 5]   #聚类簇数分别取2-5个
for n_clusters in n_clusters_list:
    est = KMeans(n_clusters=n_clusters)  # 生成KMeans模型
    est.fit(X)  # 对模型进行训练
    labels = est.labels_   #获取数据点的类别标签
    fig = plt.figure(figsize=(8, 5), dpi=144)
    ax = Axes3D(fig, rect=[0, 0, 0.95, 1], elev=48, azim=134)  #设置仰角为48度,设置方位角为134度
    ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=labels, edgecolor='black')  #画散点图，不同类别用不同颜色表示,数据点边缘设为黑色
    # ax.w_xaxis.set_ticklabels([])
    # ax.w_yaxis.set_ticklabels([])
    # ax.w_zaxis.set_ticklabels([])
    fig.add_axes(ax)
    ax.set_xlabel('花萼宽度')
    ax.set_ylabel('萼片长度')
    ax.set_zlabel('花瓣长度')
    ax.set_title(str(n_clusters) + '类')  #设置标题
    ax.dist = 12  #设置视角的观看距离
    plt.show()
#从聚类效果看，聚类簇数为_____时聚类效果较好。

