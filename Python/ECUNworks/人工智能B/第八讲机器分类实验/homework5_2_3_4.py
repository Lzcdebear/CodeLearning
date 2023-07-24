'''
第四题

建议k值选取3
拥抱镜头和打斗镜头 特征集
电影类型          标签集
需要二值化处理
特征集归一化处理
最后得出结论 第九部电影是什么片
'''
# 导入库
import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing

# 归一化对象
minmax_scaler = MinMaxScaler()
# 二值化对象
lb = preprocessing.LabelBinarizer()
# 模型对象
k = 3
knc = KNeighborsClassifier(n_neighbors=k)

# 导入数据
filmdata = pd.read_excel(r'F:\Coding\Python\ECUNworks\人工智能B\第八讲机器分类实验\sample2.xlsx')
print(filmdata)
# -----------------------------进行数据处理-------------------------------------
filmusingdata = filmdata.dropna(axis=0,inplace=False)
filmunkowndatatemp = filmdata.iloc[filmusingdata.shape[0]:,2:4]
print(filmusingdata)
print(filmunkowndatatemp)
# 获得数据集和标签集
Xtemp = filmusingdata.iloc[:,2:4]
Ytemp = filmusingdata.iloc[:,4]
# 对数据进行二值化处理
Y = lb.fit_transform(Ytemp)
print(Y[0],Ytemp[0])
print(Y)
dongzuopian = input('动作片数值')
# 对数据集进行二值化处理
X = minmax_scaler.fit_transform(Xtemp)
filmunkowndata = minmax_scaler.transform(filmunkowndatatemp)
# 将数据集合拆分为两部分
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=69)
# -----------------------------进行模型练习------------------------------------
knc.fit(X_train,Y_train)
y_predict = knc.predict(X_test)
print(Y_test,y_predict)
# -----------------------------进行预测---------------------------------
a = knc.predict(filmunkowndata)
print(a)
if int(a) == int(dongzuopian):
    print('电影是动作片')
else:
    print('是爱情片')
