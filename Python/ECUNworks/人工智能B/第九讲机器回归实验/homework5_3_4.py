# 1. 导入库
import numpy as np
import pandas as pd
# 导入sklearn相关
from sklearn.model_selection import train_test_split  #导入train_test_split函数
from sklearn.linear_model import LinearRegression  #导入LinearRegression模块
from sklearn import linear_model #导入linear_model模块
#导入matplotlib.pyplot包
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #避免中文出现乱码
plt.rcParams['axes.unicode_minus']=False

# 散点图制作，符合线性回归模型
trytimes = [30,33,35,37,39,44,46,50]
score = [30,34,37,39,42,46,48,51]
plt.scatter(trytimes,score,color='black')
plt.show()
# 2. 加载训练数据
X = np.array(trytimes).reshape(-1,1)
y = score   #标签集
# 3. 创建线性回归模型对象
clf2 = linear_model.LinearRegression()   #创建LinearRegression类对象
# 4. 实现使用数据集训练模型
clf2.fit(X, y)    #训练回归模型
# 5. 输出拟合好的函数的系数
print(clf2.coef_)  #
# 6. 输出拟合好函数的截距
print(clf2.intercept_)  #

# 7. 设置测试集，假设测试的是6元-14元间的销量
# X_test=np.arange(6,15)[:,np.newaxis]
X_test=np.array([47,55]).reshape(-1,1)
# 8. 使用测试集实现预测
y_pred = clf2.predict(X_test)  #
print(y_pred.round(0).astype(int))

# 9. 展示图像
plt.scatter(trytimes,score,color='black')
plt.scatter(X_test,y_pred,color='red')
plt.plot(trytimes, score, color='blue', linewidth=3)
trytimes=[30,33,35,37,39,44,46,50,47,55]
plt.plot(trytimes, clf2.predict(np.array(trytimes).reshape(-1,1)), color='green', linewidth=3)
plt.show()