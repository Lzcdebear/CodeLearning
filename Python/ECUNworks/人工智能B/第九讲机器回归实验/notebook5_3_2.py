# 第二题 实现多元线性回归
# （1）导入库
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import rcParams
'''
sklearn.datasets用于导入数据加载器
sklearn.model_selection用于数据选择
sklearn.linear_model用于建立回归模型
matplotlib.pyplot和rcParams用于可视化图表
'''
'''
    import pandas as pd
    import numpy as np

    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]
'''
# （2）加载数据集 
boston=load_boston()
x=boston['data']
y=boston['target']
names=boston['feature_names']
# 分割数据为训练集和测试集
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=22)
print('x_train前3行数据为：', x_train[0:3],'\n', 'y_train前3行数据为：',y_train[0:3])

# （3）创建线性回归模型对象
lr=LinearRegression()
#使用训练集训练模型
lr.fit(x_train,y_train)
#显示模型
print(lr)
#显示模型13个系数
print(lr.coef_)
#显示模型截距
print(lr.intercept_ )

# （4）使用测试集获取预测结果
print(lr.predict(x_test[:5]))

# （5）模型评估
# 计算并输出决定系数R2
print(lr.score(x_test,y_test))

# （6）绘图对比预测值和真实值
rcParams['font.sans-serif']='SimHei'
fig=plt.figure(figsize=(10,6))
y_pred=lr.predict(x_test)
plt.plot(range(y_test.shape[0]),y_test,color="blue",linewidth=1.5,linestyle="-")
plt.plot(range(y_test.shape[0]),y_pred,color="red",linewidth=1.5,linestyle="-.")
plt.legend(['真实值','预测值'])
plt.show()