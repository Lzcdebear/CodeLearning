# encoing=utf-8
'''
perprice  7 8 9 10 11 12 13
sale      120 118 112 110 108 104 102
'''
# 利用以上数据进行线性回归模型，预测其他价格销量和预计销量并画出拟合直线

# 1. 导入库
import numpy as np
from sklearn import linear_model #导入linear_model模块
#导入matplotlib.pyplot包
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #避免中文出现乱码
plt.rcParams['axes.unicode_minus']=False

# 2. 加载训练数据
# 因为训练时特征集需要是二维的，如果生成的是一维数组，需要使用np.newaxis或者reshape(1,1)转化为二维
# X = np.arange(7,14).reshape(-1,1)   #特征集
X = np.arange(7,14)[:,np.newaxis]
y = [120,118,112,110,108,104,102]   #标签集

# 3. 创建线性回归模型对象
clf = linear_model.LinearRegression()   #创建LinearRegression类对象

# 4. 实现使用数据集训练模型
clf.fit(X, y)    #训练回归模型

# 5. 输出拟合好的函数的系数
print(clf.coef_)  #

# 6. 输出拟合好函数的截距
print(clf.intercept_)  #

# 7. 设置测试集，假设测试的是6元-14元间的销量
# X_test=np.arange(6,15)[:,np.newaxis]
X_test=np.arange(6,15).reshape(-1,1)

# 8. 使用测试集实现预测
y_pred = clf.predict(X_test)  #
print(y_pred)

# 9. 绘图输出
plt.title('价格与销量关系图')
plt.xlabel('价格 (元)')
plt.ylabel('销量 (斤)')
plt.grid()#显示网格
#输出价格和销量的散点图
plt.scatter(X, y, color='black')    ###
#输出拟合直线
plt.plot(X_test,y_pred, color='blue', linewidth=3)  #
plt.show()