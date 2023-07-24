# 1. 导入库
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split  #导入train_test_split函数
from sklearn.linear_model import LinearRegression  #导入LinearRegression模块

#导入库
from sklearn.preprocessing import StandardScaler  #导入StandardScaler类
from sklearn import metrics    #导入metrics模块
from sklearn import linear_model #导入linear_model模块


# 2. 加载数据集 
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
# name 不知道怎么收集，打开网址有以下内容，就手打了
'''
 CRIM     per capita crime rate by town
 ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
 INDUS    proportion of non-retail business acres per town
 CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
 NOX      nitric oxides concentration (parts per 10 million)
 RM       average number of rooms per dwelling
 AGE      proportion of owner-occupied units built prior to 1940
 DIS      weighted distances to five Boston employment centres
 RAD      index of accessibility to radial highways
 TAX      full-value property-tax rate per $10,000
 PTRATIO  pupil-teacher ratio by town
 B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
 LSTAT    % lower status of the population
 MEDV     Median value of owner-occupied homes in $1000's
'''
x = data   #获得特征集
y = target   #获得标签集
names = np.array(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD',
       'TAX', 'PTRATIO', 'B', 'LSTAT']) #获取特征名称
print(names)

# 分割数据为训练集和测试集,设置测试集为所有样本数据的10%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=22)   ##


#标准化处理
#特征集标准化
std_x = StandardScaler()  #生成StandardScaler类对象
x_train = std_x.fit_transform(x_train)  #对训练集（特征集）应用转换规则
x_test = std_x.transform(x_test)   #对测试集（特征集）使用同样的转换规则

# （3）创建线性回归模型对象lr
lr = LinearRegression()

# 使用训练集训练模型
lr.fit(x_train, y_train)    #训练回归模型
# 显示模型
print(lr)
# 显示模型13个系数
print(lr.coef_)   #
# 显示模型截距
print(lr.intercept_)   #

# （4）对回归模型使用测试集获取预测结果
y_predict=lr.predict(x_test)   #
#输出前5个预测值。
print(y_predict) #

# （5）模型评估
# 计算并输出决定系数R2
#有两种方法
#方法1
print(lr.score(x_test, y_test))   #
#方法2
print('y_predict R2： %s' % metrics.r2_score(y_test, y_predict))  #

# 计算MSE
print("MSE（均方误差）为：%s" % metrics.mean_squared_error(y_test,y_predict))  #

