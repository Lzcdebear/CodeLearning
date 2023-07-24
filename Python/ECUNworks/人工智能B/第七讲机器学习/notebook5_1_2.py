# coding=utf-8
'''
介绍sciit-learn
内置了多种数据集，只需调用对应的数据导入方式，就可完成数据的加载
这些数据的导入方法的命名规则是
sklearn.datasets.load_<name>
这里的<name>激素hi对应的数据集名称
'''
'''
load_boston()           波士顿房价数据集
load_breast_cancer()    乳腺癌数据集
load_iris()             鸢尾花数据集
load_diabetes()         糖尿病数据集
load_digits()           手写数字数据集
load_linnerud()         体能训练数据集
load_wine()             红酒品类数据集
'''
# 导入sklearn内置boston数据集并打印其中前五行前五列数据
# 导入scikit-learn库中的load_boston函数
from sklearn.datasets import load_boston
# 导入数据集
boston = load_boston()
X = boston.data[:5, :5]
print(X)

'''
数据的归一化
同一数据集中，不同列的数据往往有着完全不同的含义，数值大小差异很大，可能会影响数据处理的最终结果，因此常常需要把每列数据都映射到0-1范围之内处理，即归一化。
scikit-learn库提供了对数据进行归一化的处理，其中preprocessing.MinMaxScaler类实现了将数据缩放到一个指定的最大值和最小值（通常是1-0）之间的功能。
它又被称为离差标准化，是对原始数据的线性变换。
MinMaxScaler类的fit_transform()函数用于把转换器实例应用到数据上，并返回转换后的数据，其格式如下
fit_transform(X,...)
其中，X可以表示数组、稀疏矩阵或DataFrame。
'''
# 对boston数据集前五行五列数据进行归一化并打印显示
# 导入库
from sklearn.datasets import load_boston
from sklearn.preprocessing import MinMaxScaler
# 导入数据集
boston = load_boston()
X = boston.data[:5, :5]
# 转换器实例化
minmax_scaler = MinMaxScaler()
# 数据归一化
boston_minmax = minmax_scaler.fit_transform(X)
print(boston_minmax)

'''
数据的标准化
scikit-learn库提供了对数据进行标准化处理的函数
包括Z-score标准化、稀疏数据标准化和带离群值的标准化。
其中，Z-Score方法可以在大多数类型的数据上得到较好的应用，标准化后得到的数据是以0为均值，1为方差的正态分布。但由于它是一种中心化的方法，将会对原始数据的分布结构产生改变。
scikit-learn库中preprocessing.StandardScaler类实现了Z-Score标准化。
'''
# 对boston数据集前五行五列数据进行z-Score标准化并打印显示
# 导入库
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
# 导入数据集
boston = load_boston()
X = boston.data[:5, :5]
# 转换器实例化
standerd_scaler = StandardScaler()
# 数据标准化
boston_standerd = standerd_scaler.fit_transform(X)
print(boston_standerd)

'''
数据的正则化
scikit-learn库提供了对数据进行正则化处理的函数
其中preprocessing.Normalizer类实现了将单个样本缩放到单位范数的功能。
在数据集之间各个指标有共同重要比率的关系时，正则化处理有比较好的效果。
'''
# 对boston数据集的前五行五列数据进行正则化并打印显示
# 导入库
from sklearn.datasets import load_boston
from sklearn.preprocessing import Normalizer
# 导入数据集
boston = load_boston()
X = boston.data[:5, :5]
# 转换器实例化
normalizer_scaler = Normalizer()
# 数据正则化
boston_normalizer = normalizer_scaler.fit_transform(X)
print(boston_normalizer)

'''
标准二值化
二值化指将数值特征向量转换为布尔类型向量
通过人为设定阈值的方式，将大于阈值的数值映射为1，而小于或等于阈值的数值映射为0。
标签二值化是二值化的重要应用之一，
标签二值化可以把非数字化的数据标签转化为数字化形式的数据标签
例如可把“Yes”和“No”等文本标签转化为“1”和“0”的数字化形式。
'''
# 对 yes no 两类标签进行二值化处理并打印显示
# 导入库
from sklearn import preprocessing
# 设置数据集
label = ['Yes', 'No', 'Yes', 'No', 'No']
lb = preprocessing.LabelBinarizer()
# 标签数据二值化
label_bin = lb.fit_transform(label)
print(label_bin)