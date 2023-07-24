'''
实验题1
1 表示是
0 表示不是

1.使用knn分类器对文件中的数据进行分类并评测结果

2.将特征集数据归一化后再使用knn分类并评测其结果

3.使用训练好的模型对新样本进行分类
'''
# 1
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = pd.read_csv(r'F:\Coding\Python\ECUNworks\人工智能B\第八讲机器分类实验\diabetes.csv',encoding='GBK')
print(data)
#获取特征集及标签集
X = data.iloc[:,:8]  #获得属性
Y = data.iloc[:,8]  #获得标签
#将数据集切分为训练集和测试集(比例为80%和20%)。
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=22); # 切分数据集，random_state=22 
# （3）利用KNN模型进行分类
knc = KNeighborsClassifier()
#使用训练集训练模型
knc.fit(X_train, Y_train)
#使用训练好的模型预测测试数据
y_predict = knc.predict(X_test)
print(y_predict)
# （4）使用模型自带的评估函数进行准确性测评。
print('The accuracy of K-Nearest Neighbor Classifier is', knc.score(X_test, Y_test))   #
# （5）使用sklearn.metrics里面的classification_report模块对预测结果做更加详细的分析。
print(classification_report(Y_test,y_predict))


# 2
#导入MinMaxScaler类用于归一化
from sklearn.preprocessing import MinMaxScaler  #
# 生成MinMaxScaler类实例化
minmax_scaler = MinMaxScaler() #
# 数据归一化
X1 = minmax_scaler.fit_transform(X) #
print(X1)
#将数据集切分为训练集和测试集(比例为80%和20%)
X_train, X_test, Y_train, Y_test = train_test_split(X1, Y, test_size=0.2, random_state=22);  ## 切分数据集 
# 利用KNN模型进行分类
knc = KNeighborsClassifier()  #
#使用训练集训练模型
knc.fit(X_train, Y_train) #
#使用训练好的模型预测测试数据
y_predict = knc.predict(X_test) #
print(y_predict)
# 使用模型自带的评估函数进行准确性测评。
print('The accuracy of K-Nearest Neighbor Classifier is', knc.score(X_test, Y_test)) #
# 使用sklearn.metrics里面的classification_report模块对预测结果做更加详细的分析。
print(classification_report(Y_test,y_predict))



# 3
# （2） 加载数据，并进行数据的分割
data2 = pd.read_excel(r'F:\Coding\Python\ECUNworks\人工智能B\第八讲机器分类实验\sample1.xlsx',sheet_name="Sheet1").iloc[:,:8]  #
print(data2)

# 数据归一化
data2_minmax = minmax_scaler.transform(data2)  #将前面生成的归一化实例规则应用于新的数据，注意不需要重新生成规则
print(data2_minmax)

#使用训练好的模型预测测试数据
y_predict2 = knc.predict(data2_minmax)  #
print(y_predict2)

#结论
print('患者1（59岁）判断为   有   糖尿病   #有、无')
print('患者2（27岁）判断为   无   糖尿病   #有、无')      
