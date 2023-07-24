'''
使用py进行线性回归的方法一般是
利用Python实现线性回归分析的基本步骤如下：  
1 依次导入相关库。  
2 数据预处理：导入或者读取数据集，必要时将分类数据数字化，划分数据集为训练集和测试集。  
3 在训练集上训练线性回归模型。  
4 在测试集上预测结果。  
5 模型评估。  
6结果可视化对比。
'''
# 第一部分 实现一元线性回归
'''
糖尿病数据集由sklearn提供
该数据集包含442个糖尿病病例的10项检查数据
以及这些病例检查后一年疾病进展的定量测量结果。 
数据集有442行记录，11列。
其中前10列为10个特征的检查数据，
10个特征分别为：年龄，性别，体重指数，
平均血压以及6个血清学测量值S1，S2，S3，S4，S5，S6，
特征取值范围为(-0.2,0.2)。第11列标签列为一年后的定量测量值。
标签取值范围是\[25,346]。
我们可以通过以下代码加载和查看该数据集：
'''
from sklearn import datasets  
# 加载数据集
diabetes = datasets.load_diabetes() 
# 显示其描述
print("【描述】\n", diabetes.DESCR)
# 显示其特征名称
print("【特征名称】\n", diabetes.feature_names)
# 显示其特征数据
print("【数据】\n", diabetes.data)
# 显示其标签数据
print("【目标值】\n", diabetes.target)

'''
补充一下 np.newaxis
X = NP.ARRAY
    (
    [1, 2, 3, 4]
    [5, 6, 7, 8]
    [9,10,11,12]
    )
x[:,2] = [3,7,11]
x[:,2][:,np.newaxis] = x[:,np.newaxis,2] =  [
                                                [3]
                                                [7]
                                                [11]
                                            ]
'''
# （1）导入库
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# （2）加载糖尿病数据集 
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
# 只使用糖尿病数据集的第三个特征
diabetes_X = diabetes_X[:, np.newaxis, 2]
# 分割数据为训练集和测试集
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
# 分割目标数据为训练集和测试集
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

#（3）创建线性回归模型对象
regr = linear_model.LinearRegression()
#使用训练集训练模型，拟合直线
regr.fit(diabetes_X_train, diabetes_y_train)

#（4）使用测试集实现预测
diabetes_y_pred = regr.predict(diabetes_X_test)
#输出回归系数
print('Coefficients:', regr.coef_)

#（5）模型评估
# 计算并输出均方差
print('Mean squared error: %.2f' % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# 计算并输出决定系数R2 
print('Coefficient of determination: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

#（6）绘图输出
plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)
plt.show()