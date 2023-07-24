# coding=utf-8
from string import printable
import pandas as pd
import csv
import numpy as np

'''
4.3.2 数据统计分析
统计函数
  Pandas的数据结构继承了NumPy的统计函数（表4-1-5），可以对表格数据的某行、某列、多行、多列或条件筛选出来的数值数据，进行统计分析。
'''

boston_new=pd.read_csv(r'F:\\Python\\ECUNworks\\人工智能B\\第四讲数据预处理\\Boston_analysis.csv')
print(boston_new)

# 求每列的平均值
print(boston_new.mean(axis=0))

# 求住宅平均房间数（RM）的最大值和最小值
print(boston_new['RM'].max(),boston_new['RM'].min())

# 统计城镇人均犯罪率（CRIM）小于0.1的记录。
# 先条件筛选得到符合条件的DataFrame对象，再对CRIM列计数，得到记录数。
print(boston_new[boston_new['CRIM']<0.1]['CRIM'].count())

'''
2. 分组运算
表格数据的分组统计是指先将表格的数据按某种规则分成若干组，
例如一个职工信息表格可以按性别将职工分为男和女两组，或者按部门分为若干组。分好组后，再按小组分别进行统计计算，例如统计部门人数等。

  DataFrame类提供groupby()函数将DataFrame对象分为若干组，返回一个groupby对象，函数使用方法如下：
  DataFrame.groupby(by=None, axis=0,…)

  其中，by表示分组依据，通常为列索引列表；axis表示按行分组还是按列分组，值为0表示按行分组，值为1表示按列分组，默认值为0。
  groupby函数按key值分组后，返回groupby对象。再对groupby对象应用统计函数或自定义函数进行计算。
'''

athletes=pd.read_csv(r'F:\\Python\\ECUNworks\\人工智能B\\第四讲数据预处理\\volleyball_analysis.csv')

# 按国籍对athletes对象分组
grouped=athletes.groupby(by=["国籍"])
print(grouped)

# 统计每组的记录数
print(grouped.size())

# 统计每组扣球的平均值
print(grouped['扣球'].mean())

# 统计每组各列的中位值
print(grouped.median())
