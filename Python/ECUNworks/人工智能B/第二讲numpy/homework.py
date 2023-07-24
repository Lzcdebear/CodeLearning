# coding=utf-8
from xml.dom.minidom import DocumentType
import numpy as np

# 第一部分
'''
第一题：创建一个从[100,200)的二维偶数序列，每行10个
'''
fnum = np.arange(100,200,2)
fnum = np.reshape(fnum,(5,10))
print(fnum)

'''
第二题：创建一个数值在50~100之间的5*8的二维整数数组
'''
snum = np.random.randint(50,100,40)
snum = np.reshape(snum,(5,8))
print(snum)

'''
第三题：3.5公里的路段每隔0.7公里设置一路桩，创建路桩的位置数组
'''
tnum = np.arange(0,3.6,0.7)
print(tnum)

'''
第四题：创建一个3行、5列的均值为1.6，方差为0.3的正态分布的随机数组
'''
forthnum = np.random.normal(1.6,0.3,(3,5))
print(forthnum)

'''
第五题：创建一个5*5的单位矩阵
'''
fifthnum = np.eye(5,5)
print(fifthnum)

# 第二部分
'''
将列表转化为数组
'''
L=[[ 2.73351472,  0.47539713,  3.63280356,  1.4787706 ,  3.13661701],
       [ 1.40305914,  2.27134829,  2.73437132,  1.88939679,  0.0384238 ],
       [ 1.56666697, -0.40088431,  0.54893762,  3.3776724 ,  2.27490386]]
l = np.array(L)

print(l[:,1])


print(l[1:3,2:5])


print(l[0:3:2,1::2])


a = np.array(l[2.5<=l])
print(np.array(a[a<=3.5]))


print(np.hstack((np.array(l[l>3]),np.array(l[l<0]))))