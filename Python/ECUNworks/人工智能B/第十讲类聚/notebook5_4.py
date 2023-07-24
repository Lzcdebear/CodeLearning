#（1）导入库
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

#（2）生成样本数据
samples = np.array([[1,1],[2,2],[3,1],[6,4],[7,5],[8,4]])

#（3）把样本数据显示在二维坐标上
plt.figure(figsize=(8,5),dpi=144)
plt.scatter(samples[:,0],samples[:,1],s=100)

#（4）使用KMeans模型拟合
est=KMeans(n_clusters=2)
est.fit(samples)

#（5）将聚类结果利用散点图显示出来
labels=est.labels_
centers=est.cluster_centers_
fig=plt.figure(figsize=(8,5),dpi=144)
plt.scatter(samples[:,0],samples[:,1],s=100,c=labels.astype(np.float))
plt.scatter(centers[:,0],centers[:,1],s=100,marker="*")
plt.show()


# 第二部分
#（1）导入库
from sklearn.datasets import make_blobs #生成素数分布的Blobs数据集--X数组、blob_std列表、n_samples
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
#（2）利用scikit-learn中的make_blobs函数生成样本数据集
X,Y=make_blobs(n_samples=1000,centers=2)
#（3）利用散点图的形式将样本数据展示出来
plt.figure(figsize=(8,5),dpi=144)
plt.scatter(X[:,0],X[:,1],s=50,edgecolor='k')
plt.show()
#（4）使用KMeans模型拟合，聚类数设为4。
kmean=KMeans(4)
kmean.fit(X)
#（5）将聚类结果利用散点图显示出来
labels=kmean.labels_
centers=kmean.cluster_centers_
fig=plt.figure(figsize=(8,5),dpi=144)
plt.scatter(X[:,0],X[:,1],c=labels.astype(int),s=50,edgecolor='k')#显示聚类结果
plt.scatter(centers[:,0],centers[:,1],c='r',s=100,marker="*")#显示质心
plt.show()

# 第三部分
#（1）导入库
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn import datasets
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #避免中文出现乱码
#（2）导入Iris数据
iris=datasets.load_iris()#导入iris数据
X=iris.data
#（3）使用KMeans模型拟合，聚类数设为3
est=KMeans(n_clusters=3)
est.fit(X)
#（4）选取其中的三个维度，并显示其聚类结果
labels=est.labels_
fig=plt.figure(figsize=(8,5),dpi=144) 
ax=Axes3D(fig,elev=48,azim=134)
ax.scatter(X[:,3],X[:,0],X[:,2],c=labels.astype(np.float),edgecolor='k')
ax.set_xlabel('花萼宽度')
ax.set_ylabel('萼片长度')
ax.set_zlabel('花瓣长度')
ax.set_title('Iris数据集的聚类展示')
ax.dist=12
plt.show()
