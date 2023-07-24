'''
第二个实验
利用 sklearn 中的 make_bolbs() 函数生成随机150个样本
样本数据特征值为2个
然后利用knn分类器进行分析与预测
'''
# 导入库
# （1）导入库
from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier   #导入KNeighborsClassifier类
from sklearn.model_selection import train_test_split   #导入train_test_split方法
from sklearn.metrics import classification_report   #导入classification_report模块
# （2）利用make_blobs函数生成150个样本数据，特征数为2的数据
X, Y = make_blobs(n_samples=150, n_features=2)
# （3）利用散点图展示出来
plt.figure(figsize=(6, 4), dpi=144)
plt.xticks(())
plt.yticks(())
plt.scatter(X[:,0], X[:,1], s=20, marker='o');  #用散点图画出每个样本的两个属性
plt.show()
#将数据集切分为训练集和测试集(比例为80%和20%)。
X_train, X_test, Y_train, Y_test =  train_test_split(X,Y,test_size=0.2);  # 切分训练集、测试集为8：2
# （3）利用KNN模型进行分类
knc = KNeighborsClassifier()  #生成K分类器实例
knc.fit(X_train,Y_train)   #使用训练数据训练分类器模型
y_predict = knc.predict(X_test)   #验证训练好的模型
# （4）使用模型自带的评估函数进行准确性测评。
print('The accuracy of K-Nearest Neighbor Classifier is', knc.score(X_test, Y_test)) #
# （5）使用sklearn.metrics里面的classification_report模块对预测结果做更加详细的分析。
print(classification_report(Y_test,y_predict)) #

