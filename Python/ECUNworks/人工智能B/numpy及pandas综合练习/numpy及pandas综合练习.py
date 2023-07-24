# coding=utf-8
import numpy as np
import pandas as pd

# 第一部分：numpy练习
'''
1. 归一化问题
(1)创建一个由10到20（不含）之间的随机整数组成的5*5二维NumPy数组Z；
(2)将数组元素归一化到0~1，即最小的变成0，最大的变成1。
'''

Z = np.random.randint(10,21,(5,5))  #创建一个由10到20之间的随机整数组成的5*5二维NumPy数组Z
print("矩阵 Z=\n", Z)
Zmin = Z.min()  #取最小值
Zmax = Z.max()  #取最大值
Z = (Z - Zmin) / (Zmax - Zmin)
print("归一化后的Z：\n", Z)


'''
2. 二维数组的查询
(1)创建一个由1~16的整数按顺序组成的一维NumPy数组对象,再变换为4*4二维数组对象arr；
(2)使用索引的方式获取arr数组中第二行第一列和第三行第二列的数据；
(3)使用切片方式获取arr数组中除了第一列和第一行以外的数据；
(4)使用布尔运算方式将arr数组中为奇数的数据都置为零。
'''
arr = np.array([i for i in range(1,17)]).reshape(4, 4)    #创建一个由1~16的整数组成的一维NumPy数组对象,再变换为4*4二维数组对象arr
print(arr)
num_1 = arr[1:2,0:1]  #获取arr数组中第二行（行位置索引为1）第一列元素（列位置索引为0）
num_2 = arr[2:3,1:2]  ##获取arr数组中第三行第二列元素
print(num_1, num_2)
arr2 = arr[1:,1:]  #获取arr数组中除了第一列和第一行以外的数据；
print(arr2)
mask = (arr%2!=0)  #使用布尔运算方式找出arr数组中为奇数的数据
arr[mask] = 0  #将arr数组中为奇数的数据都置为零
print(arr)

'''
3. 二维数组的统计分析
(1)创建20到40（不含）之间均匀分布的4*5二维NumPy数组对象；
(2)计算数组中每行的平均值;计算数组中每列的最大值；
(3)返回数组中最小值的索引。
'''
arr = np.random.uniform(20,41,20).reshape(4,5)  #创建20到40之间均匀分布的4*5二维NumPy数组对象
print(arr)
row_mean = arr.mean(axis=1)  #计算数组中每行的平均值
col_max = arr.max(axis=0)  #计算数组中每列的最大值
index_max = arr.argmin()  #返回数组中最小值的索引
print(row_mean)
print(col_max)
print(index_max)

# 第二部分：pandas
'''
1. Series对象的修改
(1)创建一个存储了21~30的整数的Series对象，索引值为1~10；
(2)将其中小于等于25的元素赋值为0。
'''
data = np.array([i for i in range(21,31)]) #创建一个存储了21~30的整数的一维数组；
index = np.arange(1, 11, 1)
num = pd.Series(data,index=index) #创建一个存储了21~30的整数的Series对象，索引值为1~10；
print(num)
num[num<=25] = 0   #将其中小于等于25的元素赋值为0
print(num)

'''
2. DataFrame对象的访问和文件写入
(1)创建一个存储了用户记账金额的DataFrame对象，行索引为1月~12月，列索引为‘收入’和‘支出’，元素值为5000~10000的随机数；
(2)取出‘支出’列作为新的DataFrame对象；
(3)将该数据从新的DataFrame对象写入到CSV文件。
'''
month = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
money = np.random.randint(5000,10001,24).reshape(12,2) #生成尺寸为12*2的二维随机整数数组,元素值为5000~10000的随机数
account = pd.DataFrame(money,month , columns=['收入', '支出'])  # 创建DataFrame对象
print(account)
account_new = account['支出'] #取出‘支出’列作为新的DataFrame对象
print(account_new)
# 从DataFrame对象写入数据到CSV文件
account_new.to_csv(r'F:\Python\ECUNworks\人工智能B\numpy及pandas综合练习\account.csv')  #DataFrame对象写入到CSV文件

'''
3. DataFrame对象的删改和文件读取
(1)读取波士顿房价数据文件Boston_pandas.csv创建DataFrame数据对象；
(2)删除行索引为1~3的数据内容；修改 'MEDV' 列的数据内容为15。
'''
# 从CSV文件读取数据到DataFrame对象
boston = pd.read_csv(r'F:\Python\ECUNworks\人工智能B\numpy及pandas综合练习\Boston_pandas.csv')  #
print(boston)
# 删除行索引值为1、2和3的元素
boston = boston.drop([1, 2, 3], axis=0)  #
print(boston)
# 修改 'MEDV' 列的数据内容为15
boston['MEDV'] = 15   #
print(boston)

