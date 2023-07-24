# coding=utf-8
from string import printable
import pandas as pd
import csv
import numpy as np

'''
（1）缺失数据的清除
  dropna()函数用于删除缺失值所在的行或列，并返回新的对象，同时该函数不会改变原始对象，其格式如下：

    DataFrame.dropna (axis=0, how='any', thresh=None, inplace=False,…)

  其中，axis表示删除缺失值所在的行或者列，值为0表示删除行，值为1表示删除列
    how表示是否全为缺失值才进行移除,
           值为'any'表示行/列中只要包含缺失值就会进行移除,值为'all'表示行/列的全部值都为缺失值才会进行移除，默认值为'any'
           在扣除缺失值后行/列中还剩余一定数量的有效数据，
    thresh表示移除有效数据的个数小于thresh的行/列，thresh的类型为整数。
    inplace表示是否对当前对象进行清除，值为False表示不对当前对象进行清除，生成新对象，值为True表示对当前对象进行清除，不产生新对象，默认值为False。

'''
# 从CSV文件读取数据到DataFrame对象
boston=pd.read_csv(r'F:\\Python\\ECUNworks\\人工智能B\\第四讲数据预处理\\Boston_pandas.csv')
print(boston)

'''
在读取数据时，Pandas使用NumPy中定义的NaN来表示缺失值。Boston_pandas.csv为波士顿房价数据集，每条数据包括了房屋和周围的一些信息。
其中
CRIM（城镇人均犯罪率）、
NOX（一氧化氮浓度）
RM（一氧化氮浓度）
AGE（1940年之前建成的自用房屋比例）
LSTAT（人口中地位低下者的比例）
MEDV（自住房的平均房价）。
'''

# 移除有效数据小于5个的行
boston.dropna(thresh=5,inplace=True)
print(boston)
print('参数axis采用了默认值0，表示按照行的方向逐行检查，进行移除')
print('参数how采用了默认值any，表示当前行中只要包含缺失值就会准备进行移除；')
print('参数thresh=5，表示移除有效数据小于5个的行。')
print('观察原数据，只有索引值为2的行满足了这些条件。观察程序运行结果，果然缺少了索引值为2的行。')


'''
（2）缺失数据的填充
  fillna()函数用于批量填充缺失值，并返回新的对象，同时该函数不会改变原始对象，其常用格式如下：

    DataFrame.fillna(value,…)

  其中，value包含了需要填充的值，value的类型可以是常量、字典、Series或DataFrame。
'''

boston.fillna(value={'NOX':0.524},inplace=True)
print(boston)

'''
2. 重复数据的处理
  drop_duplicates()函数用于重复数据行，并返回新的对象，同时该函数不会改变原始对象，其格式如下：

    DataFrame .drop_duplicates(subset = None, keep= 'first', inplace = False,…)

subset表示列标签或列标签序列指定需要判定的列，默认None，判定所有的列；
keep表示以何种方式进行保留，值为'first'表示保留重复行中第一次出现的行，值为'last'表示保留重复行中最后一次出现的行，值为False表示删除所有重复的行，默认值为'first'。
inplace表示是否对当前对象进行清除，值为False表示不对当前对象进行清除，生成新对象，值为True表示对当前对象进行清除，不产生新对象，默认值为False。
'''

boston.drop_duplicates(inplace=True)
print(boston)

