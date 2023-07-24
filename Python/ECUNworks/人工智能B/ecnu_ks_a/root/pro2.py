# 导入必要的库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, preprocessing, model_selection, neighbors, metrics

# 从键盘输入随机数编号n，示例中n=42
n = int(input("请输入随机数编号：\n"))

# 加载并导入手写数字数据集
digits = datasets.load_digits()
X = digits
y = digits

# 实例化转换器并对X进行数据标准化
standard_scaller = preprocessing.StandardScaler()
X_scaled = standard_scaller.fit(X)
# 划分训练集和测试集，测试样本占30%，随机数编号为n
random_state = 42
X_train, X_test, y_train,y_test= model_selection.train_test_split(X_scaled,y,test_size=0.3,random_state=random_state)
# 创建KNN分类器并在训练集上进行训练，最邻点数量为5，并在测试集上对结果进行预测
k = 5
knn = neighbors.KNeighborsClassifier(n_neighbors=n)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
# 计算精确率并输出混淆矩阵，其中精确率评价值的平均值计算方式average设为'macro'，保留四位小数
precision = metrics.precision_score(y_test,y_pred,average='macro')
print('精确率：{:.4f}'.format(precision))

# 输出混淆矩阵
confusion = metrics.confusion_matrix(y_test, y_pred)
print("混淆矩阵：")
print(confusion)
