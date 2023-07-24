from html.entities import name2codepoint
import numpy as np
import csv
from cmath import pi
import pandas as pd

def bcal(n):
    a = 4 * pi * (10 ** -7) * 500 * 0.01 * 0.1
    n2 = (n/100) * (n/100)
    b = 2 * ((0.01 + n2) ** (1.5))
    fin = a/b
    return fin




libdata = []
teodata = []
findata = []
a = 1.12
x = float(input('输入一个数值'))
while x != 0:
    libdata.append(x)
    x = float(input('输入一个数值'))
print(libdata)
for i in range(-12,13,1):
    a = bcal(i)
    teodata.append(a)
print(teodata)

for h in libdata:
    findata.append(h)
for h in teodata:
    findata.append(h)
findata = np.array(findata)
findata.reshape(2,25)
print(findata)
f = open("F:\Python\亥姆霍兹的磁场分布\data.csv",'w')
try:
    writer = csv.writer(f)	#构造writer对象
    writer.writerow(libdata)	#写入标题行
    writer.writerow(teodata)	#写入数据行
finally:
    f.close()	#关闭文件

