# 1. 导入库
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split  #导入train_test_split函数
from sklearn.linear_model import LinearRegression  #导入LinearRegression模块

#导入库
from sklearn.preprocessing import StandardScaler  #导入StandardScaler类
from sklearn import metrics    #导入metrics模块
from sklearn import linear_model #导入linear_model模块


X = np.array([173, 155, 160, 165, 170, 175, 180, 170, 190, 180]).reshape(-1,1)
y = [170, 162, 164, 169, 175, 178, 185, 172, 180, 175]   #标签集

# 3. 创建线性回归模型对象
clf = linear_model.LinearRegression()   #创建LinearRegression类对象
# 4. 实现使用数据集训练模型
clf.fit(X, y)    #训练回归模型
# 8. 使用测试集实现预测
y_pred = clf.predict(np.array([170]).reshape(-1,1))  #
print(y_pred)
