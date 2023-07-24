# coding=utf-8
from unittest import skip
import pandas as pd
import numpy as np

'''
第一部分
(1)准备数据 rainfalldata.csv文件中存放了多个城市12个月的降水量
'''
# 读入rainfalldata.csv文件到DataFrame对象
df=pd.read_csv(r'F:\Python\ECUNworks\人工智能B\第六讲综合作业\rainfalldata.csv',encoding='gbk')  #
print(df)

# 求每个城市的平均降水量
city_ave_rain = df.mean(axis=1)
print(city_ave_rain)

# 求每个月的平均降水量
month_ave_rain = df.mean(axis=0)
print(month_ave_rain)

# 求每个城市最大降水量和最小降水量出现的月份
city_max_rain = df.iloc[:,1:].astype('float64').idxmax(axis=1,skipna=True)
print(city_max_rain)
city_min_rain = df.iloc[:,1:].astype('float64').idxmin(axis=1,skipna=True)
print(city_min_rain)

# np.array([df.loc[city,'1月':].astype("int").argmin()+1 for city in range(9)]) # not mine
# np.array([df.loc[city,'1月':].astype("int").argmax()+1 for city in range(9)]) # not mine

# 求出现降水量最高的城市
city_sum_rain = df.sum(axis=1)
rain_max_city = city_sum_rain.argmax()
print(df.iloc[rain_max_city-1,0])

