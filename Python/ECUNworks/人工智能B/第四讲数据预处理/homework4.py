# coding=utf-8
import pandas as pd
import numpy as np
import csv


# (1) 创建表示10×10的随机矩阵的DataFrame对象，行索引和列索引都为1-10，元素取值在0-100
data = np.random.randint(0,101,(10,10), np.int32)   #创建矩阵作为DF的数据（values）
index = np.arange(1, 11, 1)   #创建行列索引
matrix = pd.DataFrame(data,index,index)  # 创建DataFrame对象
print(matrix)


# 求每列的最大值和最小值
matrix_max = matrix.max(axis=0)  # 求每列最大值
print(matrix_max)
matrix_min = matrix.min(axis=0)  # 求每列最小值
print(matrix_min)


# (1) 读取素材文件fish.csv 创建DataFrame数据对象；
fish = pd.read_csv(r'F:\Python\ECUNworks\人工智能B\第四讲数据预处理\fish.csv', encoding="UTF-8")   #注意文件路径名应与你文件所在位置对应  
print(fish)

# (2) 对全部为缺失值的列进行移除；移除效果直接作用于fish对象
fish.dropna(axis=1, how='all', inplace=True)
print(fish)

# (3)对包含缺失值的行进行移除；移除效果直接作用于fish对象。
fish.dropna(axis=0,how='any',inplace=True)
print(fish)




# (1) 读取素材文件vegetable.csv 创建DataFrame数据对象；
vegetable = pd.read_csv(r'F:\Python\ECUNworks\人工智能B\第四讲数据预处理\vegetable.csv', encoding='UTF-8') 
print(vegetable)


# (2) 不改变当前对象，以保留重复行中第一次出现的行的方式删除重复行，将结果存储到新的DataFrame数据对象；
vegetable_new1 = vegetable.drop_duplicates(subset = None, keep= 'first', inplace = False)
print(vegetable_new1)

# (3) 不改变当前对象，以保留重复行中最后一次出现的行的方式删除重复行，将结果存储到新的DataFrame数据对象。
vegetable_new2 = vegetable.drop_duplicates(subset = None, keep = 'last', inplace = False)
print(vegetable_new2)



# (1) 创建包含多种动物特征数据的DataFrame数据对象，并按动物种类分组；
df = pd.DataFrame({'动物':['游隼', '鹦鹉', '猎豹', '游隼', '猎豹','游隼'], \
'速度':[380,24,120,370,130,368], '重量':[3.5,1,80,3,82,np.nan], \
'状态':['野生',np.nan,'野生','豢养','野生','豢养']}) 
print(df)

#按动物种类分组，并显示
grp=df.groupby(by=['动物'])#
print(grp.groups)

#统计DataFrame数据对象中每组动物的计数（记录数）
print(grp['动物'].value_counts())  #

# (3)对'重量'列的缺失数据，使用同类动物重量的平均值填充

# 计算每种动物重量的平均值
weight_mean=grp['重量'].mean()  #
print(weight_mean)

# 找到体重不存在的项
mask=df['重量'].isnull()
an=df.loc[mask,['动物']]   #
print(an)

#重量的缺失数据用同类动物重量的平均值填充
df.loc[mask,['重量']] = weight_mean[an['动物']]  #
print(df)