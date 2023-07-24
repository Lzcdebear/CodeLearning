# coding=utf-8
'''
对模型的评价，有助于了解其性能
通过优化可以获得更好模型，而对于不同类型的模型所采用的评价指标也不尽相同。
scikit-learn中metrics模块提供了为特定目标计算评价指标的功能
主要有分类、回归和聚类等几种。

分类常用的评价指标有
混淆矩阵 (Confusion Matrix) 、
精确率 (Precision)、
召回率 (Recall)、
F1分数 (F1 Score)
准确率 (Accuracy)等，

回归主要评价指标有
平均绝对误差(MAE，Mean Absolute Error)、
均方误差(MSE，Mean Squared Error)、
均方根误差(RMSE，Root Mean Squared Error)、R^2等。
'''

from sklearn import metrics
from sklearn.preprocessing import LabelBinarizer
lb = LabelBinarizer()
y_true = ['猫', '猫', '猫', '猫', '猫', '狗', '狗', '狗', '狗', '狗']
y_pred = ['猫', '猫', '猫', '猫', '狗', '猫', '狗', '狗', '猫', '狗']
#scikit-learn.metrics中的confusion_matrix()函数用来计算混淆矩阵，从而得出TP=4，TN=3，FP=2，FN=1，与计算结果相同。
# （1）计算混淆矩阵
print('Confusion Matrix：')
print(metrics.confusion_matrix(y_true, y_pred, labels=['猫', '狗']))
