# coding=utf-8

from itertools import dropwhile
from traceback import print_tb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#数据清洗
#读入文件RollerCoasterData.xlsx，该文件存放了世界各大乐园的著名的过山车的数据指标
df1=pd.read_excel(r'F:\Python\ECUNworks\人工智能B\第六讲综合作业\RollerCoasterData.xlsx',sheet_name='RollerCoasterData')  #
print(df1)

#删除所有“ID”列或者“Height (feet)”列有缺失数据的数据行
'''
ID0 = df1[df1.iloc[:,0].isnull()].index
HEIGHT0 = df1[df1.iloc[:,11].isnull()].index
dellist1 = ID0.append(HEIGHT0)
print(dellist1)
df1.drop(dellist1, axis=0, inplace=True)
print(df1)
'''
df1.drop(df1[df1.iloc[:,0].isnull()].index.append(df1[df1.iloc[:,11].isnull()].index), axis=0, inplace=True)#
print(df1)

#将“Height (feet)”列的值转为float
df1.iloc[:,11] = df1.iloc[:,11].astype('float64')

#统计“Height (feet)”列的平均值(保留2位小数)
#提示：可用numpy模块的round函数，格式：round(数值，小数点位数)
ave_height = round(df1.iloc[:,11].mean(axis=0),2)

#按国家/地区（Country/Region）分组统计不同国家/地区的过山车平均高度
CountryRegion = df1.groupby('Country/Region')   #按国家/地区（Country/Region）分组
ch = CountryRegion['Height (feet)'].mean()  #按分组统计不同国家/地区的过山车平均高度
print(ch)

# 画出各个国家过山车平均高度的条形图
fig, ax = plt.subplots(1, 1)
fig.set_size_inches(15, 5)
plt.rcParams['font.sans-serif'] = ['SimHei']
ax.set_xticks(np.arange(ch.size))
ax.set_xticklabels(ch.index, rotation=30, ha='right')
ax.set(title='各国家/地区过山车平均高度', xlabel='国家/地区', ylabel='高度（英尺）')
ax.bar(x=list(CountryRegion.groups.keys()), height=ch.values, color='green')
plt.show()

#统计表中各国家/地区过山车的数量
cc = CountryRegion.size()   #统计各国家/地区过山车的数量
print(cc)

#根据各国家/地区过山车的数量的占比绘制饼图
fig = plt.figure(figsize=(12,12)) #设置画面大小为12*12英寸
plt.axis('equal') #设置xy轴等刻度
plt.pie(x=cc.tolist() ,autopct='%.1f%%',labels=list(CountryRegion.groups.keys()))  #画饼图
plt.legend(cc.index, title='过山车数量占比', bbox_to_anchor=(-0.15, 0.8),fontsize='xx-small', loc="center left") #显示图例
plt.show()
