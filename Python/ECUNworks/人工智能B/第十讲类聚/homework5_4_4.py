# 实验4
# （1）导入库
import numpy as np
from sklearn.cluster import KMeans  #导入KMeans类
from matplotlib import pyplot as plt
from sklearn import datasets
from mpl_toolkits.mplot3d import Axes3D  # 这个工具包可以显示 3D 图形
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

plt.rcParams['font.sans-serif'] = ['SimHei']  # 避免中文出现乱码
plt.rcParams['axes.unicode_minus'] = False

df=pd.read_excel(r'F:\OneDrive\Coding\Python\ECUNworks\人工智能B\第十讲类聚\sample14_1.xlsx',sheet_name='Sheet1')  #
print(df)

'''
在Excel文件sample14_1.xlsx中，有20种12盎司啤酒成分和价格的数据，
请对这些数据进行聚类分类，完成以下要求：

1.对啤酒的3种成分（热量、钠含量和酒精含量）进行KMeans聚类分析，
簇数量取5，并画出3维散点图（数据要求先进行归一化）；

2.假设啤酒的风味由其成分（3种）决定，
某顾客喜欢序号为18的OLYMPIA_GOLD_LIGH啤酒，
请向他推荐他可能会喜欢的其他几款啤酒（属同一簇）。

（提示：假设数据集为X，聚类以后得到的类别标签集为labels，
其中18号啤酒的标签为a，则X[labels == a]则返回同一簇的节点。）
'''
minmaxscaler1 = MinMaxScaler()
df_minmax_scalered = minmaxscaler1.fit_transform(df.iloc[:,1:])
kmeans1 = KMeans(n_clusters=5)
kmeans1.fit(df_minmax_scalered)
labels = kmeans1.labels_
centers = kmeans1.cluster_centers_
# print(df_minmax_scalered)
# print(labels)  # cluster labels for each row in data frame

fig = plt.figure(figsize=(10,10))  # 画布大小为10x10
ax = Axes3D(fig, [0.1, 0.1, 0.8, 0.8])
ax.scatter(df_minmax_scalered[:,0],df_minmax_scalered[:,1],df_minmax_scalered[:,2],c=labels)
fig.add_axes(ax)
ax.set_xlabel('热量')
ax.set_ylabel('钠含量')
ax.set_zlabel('酒精含量')
ax.set_title('我也不知道应该叫什么所以就不取名字了')  #设置标题
plt.show()

print(labels[17])
print(df[labels == labels[17]].iloc[:,0])
