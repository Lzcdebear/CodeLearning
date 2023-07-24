# coding=utf-8
import pandas as pd
import numpy as np

ar  = np.random.uniform(1,51,25).reshape(5,5)
frame = pd.DataFrame(ar)

# from sklear import preprocessing 归一化 正则化
from sklearn.preprocessing import MinMaxScaler # 导入库用于数据归一化
from sklearn.preprocessing import Normalizer   # 导入库用于数据正则化

# minmaxscaler the dataframe
# 转换器实例化
minmax_scaler = MinMaxScaler()  #
# 数据归一化
minmax_result = minmax_scaler.fit_transform(frame)  #
print("数据归一化：\n", minmax_result)

# 转换器实例化
normalizer_scaler = Normalizer() #
# 数据正则化
normalizer_result = normalizer_scaler.fit_transform(frame)  #
print("数据正则化：\n", normalizer_result)
# train set test set
# from sklearn model_selection import trainset and testset
from sklearn.model_selection import train_test_split
# set string sample
s = "机器学习的研究涉及概率论统计学逼近论凸分析算法复杂度理论多门学科是人工智能的核心"
# set feature set and label set
X, y = list(s), range(40)
# The ratio of the test set to the training set is set to 2:8, 
# and the random number identifier is set to 8, 
# ensuring that the same split results can be obtained in repeated experiments.
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=8)  #
print("测试集:", X_test)
# calculate evaluation metrics
from sklearn import metrics
#导入标签二值化处理模块preprocessing.LabelBinarizer类
from sklearn import preprocessing  #
#生成LabelBinarizer类的对象
lb = preprocessing.LabelBinarizer()  #
#真值和预测值
y_true = ['男', '女', '男', '男', '男', '女', '女', '女','男', '女']    #真值
y_pred = ['男', '男', '男', '男', '女', '男', '女', '女', '男', '女']   #预测值
#手工计算混淆矩阵（假设要判断的是“是否是男”）
TP=4          #预测正确，预测类别为“男”的样本数
FP=1          #预测错误，预测类别为“男”的样本数
FN=2          #预测错误，预测类别为“女”的样本数
TN=3          #预测正确，预测类别为“女”的样本数
matrix=[[4,2],[1,3]]   #混淆矩阵[[TP,FN],[FP,TN]] 
# 计算混淆矩阵
print('Confusion Matrix：')
print(metrics.confusion_matrix(y_true, y_pred, labels=['男', '女']))   ###
#手工计算分类的4个指标
#手工计算时请给出中间步骤
ACC=(4+3)/(4+1+2+3)     #准确率（Accuracy）=(TP+TN)/(TP+TN+FP+FN)
P = 4/(4+1)             #精确率（Precision）=TP/(TP+FP)
R = 4/(4+2)             #召回率（Recall）=TP/(TP+FN)
F1 =(2*(4/5)*(4/6))/((4/5)+(4/6))       #F1分数（F1 Score）=2*P*R/(P+R)
# 利用LabelBinarizer对象将标签二值化，再分别计算精确率、召回率、F1分数和准确率
y_true_binarized = lb.fit_transform(np.array(y_true))
y_pred_binarized = lb.fit_transform(np.array(y_pred))
print('准确率ACC： %s' % metrics.precision_score(y_true_binarized, y_pred_binarized))
print('精确率P： %s' % metrics.recall_score(y_true_binarized, y_pred_binarized))
print('召回率R： %s' % metrics.f1_score(y_true_binarized, y_pred_binarized))
print('F1分数：%s' % metrics.accuracy_score(y_true_binarized, y_pred_binarized))
# 利用classification_report()函数实现对精确率、召回率、F1分数和准确率的计算
print('Classification Report：')
print(metrics.classification_report(y_true,y_pred)) #

# 综合应用
'''
小明和小张想对某股票的价格进行回归分析
已经获得了某股票在一段时间内的收盘价
两人分别用不同次数的多项式对收盘价进行拟合
（小明用3次多项式，小张用5次多项式）
请根据回归评价指标MAE、MSE等判断两人中谁的方法更好。
'''
# prepare data
import numpy as np
#polyfit()函数可以对一组数据使用多项式函数进行拟合，找到和这组数据最接近的多项式的系数
#第一步：
x = np.arange(1,28)
#第二步：某股票在28个交易日的收盘价
y = [17.89,18.47,19.04,18.61,18.25,18.23,17,18.22,18.19,18.33,18.42,18.58,18.46,
     17.59,17.6,17.75,16.98,16.67,16.92,16.77,16.85,16.74,16.71,16.34,16.11,15.81,17.57]
y = np.array(y)
#第三步：将目标函数的数组传递给polyfit()进行拟合，
#第三个参数arg为多项式函数的最高阶数。
#polyfit()所得到的多项式和目标函数在给定的1000个点之间的误差最小，
#polyfit()返回多项式的系数数组。
f3 = np.polyfit(x, y, 3)     #小明
f5 = np.polyfit(x, y, 5)     #小张
#根据多项式系数得到多项式函数
pf3 = np.poly1d(f3)
print(pf3)
pf5 = np.poly1d(f5)
print(pf5)
#小明的拟合结果
y1=pf3(x)
print(y1)
#小张的拟合结果
y2=pf5(x)
print(y2)

# calculate regression evaluation metrics.
from sklearn import metrics    #
# 计算MAE
print('MAE：')
print('小明的MAE： %s' % metrics.mean_absolute_error(y,y1))  #
print('小张的MAE： %s' % metrics.mean_absolute_error(y,y2))  #
# 计算MSE
print('MSE：')
print('小明的MSE： %s' % metrics.mean_squared_error(y,y1)) #
print('小张的MSE： %s' % metrics.mean_squared_error(y,y2)) #
# 计算决定系数
print('R2：')
print('小明的R2： %s' % metrics.r2_score(y,y1)) #
print('小张的R2：%s' % metrics.r2_score(y,y2)) #