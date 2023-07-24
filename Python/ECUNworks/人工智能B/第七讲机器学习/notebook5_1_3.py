# coding=utf-8
'''
为了更好的评测模型的效果，通常将原始数据集划分为训练集（train set）和测试集（test set）两部分：
训练集是训练机器学习算法的数据集；
测试集是用来评估经训练后的模型性能的数据集。
cikit-learn.model_selection中的train_test_split()函数提供了将数据集进行切分的功能
其格式如下所示：
机器学习的数据一般是由特征（feature）和标签（label）两部分组成。

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size, random_state, shuffle)

其中X是特征集，y是标签集
X_train和y_train分别代表训练集的特征和标签
X_test和y_test分别代表测试集的特征和标签
test_size表示测试集所占数据集的比例，取值范围为0~1
random_state表示随机数种子。
shuffle表示数据集在切分前是否需要重排，默认True。
'''
# Example
# 导入库
from sklearn.model_selection import train_test_split
# 设置数据集
X, y = ['我', '是', '中', '国', '人'], range(5)
'''
shuffle=False表明数据集中的记录顺序在切分前不需要重排运行多次的结果也是一样
shuffle=True，则数据集中的记录顺序在切分前顺序被打乱,得到的测试集的结果是随机的
但通过设置random_state可以获得同样的切分结果。
'''
# （1）参数shuffle的作用，打印测试集的结果
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, shuffle=False)
print(X_test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, shuffle=False)
print(X_test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, shuffle=True)
print(X_test)
'''
random_state的值是该组随机数的编号
当值相同时，在重复试验中可保证得到相同的切分结果(random_state=8的两段代码输出测试集结果相同)；
当随机数种子不同时，切分结果也不同
(random_state=8和random_state=10的两段代码输出测试集的结果不同)。
'''
# （2）参数random_state的作用，打印测试集的结果
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=8)
print(X_test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=10)
print(X_test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=8)
print(X_test)