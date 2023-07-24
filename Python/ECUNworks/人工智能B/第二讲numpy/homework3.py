# coding=utf-8
import csv
from unicodedata import decimal
import numpy as np

L=[]
city=[]
with open("F:\\Python\\第二讲作业\\rainfalldata.csv") as f:
    lines=list(csv.reader(f))
    lines.pop(0)
    
    for line in lines:
        city.append(line[0])
        L.append([int(x) for x in line[1:] ])
print(city)
print(L)

leng = len(city)
raindata = np.array(L)
raindata = np.reshape(raindata,(leng,12))
print(raindata)

'''
求每个城市的平均降水量
'''
print(np.around(raindata.mean(axis=1),decimals=2))

'''
求每个月的平均降水量
'''
print(np.around(raindata.mean(axis=0),decimals=2))

'''
求每个城市最大降水量和最小降水量在几月份
'''
print(raindata.argmax(axis=1)+1)
print(raindata.argmin(axis=1)+1)

'''
求每个月降水最高的城市
'''
rainmaxcity = raindata.argmax(axis=0)
print(rainmaxcity)
raincity = []
for i in rainmaxcity:
    raincity.append(city[i])
print(raincity)
