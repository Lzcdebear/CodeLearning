# coding=utf-8
"""numpy 的使用方式
函数说明，使用方式为 变量.函数

ndim
返回整数 表示多维数组的维数

shape
返回整数元组，表示多维数组的尺寸，例如“n行m列”返回(n,m)

size
返回整数，表示多维数组总的元素个数

dtype
返回 data-type，表示多维数组元素的数据类型

itemsize
返回整数，表示数组中每个元组的字节大小
"""

from cgi import print_arguments
from string import printable
import numpy as np

print('numpy的数组array创建方式')
places = np.array(['松江','上海','北京','杭州'])
print(places)
print(places.ndim)
print(places.size)
print(places.dtype)
"""
numpy中还可以使用arange进行数组的创建
arange和range函数是一样的，使用的时候(start,stop,step,dtype=None)
和range不一样的是arange可以创建浮点型的函数
注意这里的 stop 和 range 一样不包括 stop 这个数值
"""
num1=np.arange(1,10)
num1.dtype  #查看num1对象的数据类型
num2=np.arange(1.0,10.0)
num2.dtype  #查看num2对象的数据类型
print(num1)
print(num2)
"""
还可以使用 linspace 进行创建一维数组
创建的数组是等间距的，创建方式
numpy.linspace(start,stop,num=数字)
注意这里的stop是包括在数值里面的
同样，linspace也是可以使用浮点数的
"""
print(np.linspace(1,10,4))
print(np.linspace(1,10,6))
print(np.linspace(2.5,15.5,8))
"""
注意在 print 这个等间距数组的时候，每个数字占用的长度和数字与数字之间的间隔是一定的
例如
1.2  __1.356__2.565__
1.2后面空格数量会增加
"""

"""
array还可以基于python的列表嵌套成为二维数组
具体方式和之前是一样的
"""
scores=np.array([[96,73,78],[90,89,92],[60,70,83]])
print(scores)
scores.ndim #查看scores对象的维度数目
scores.size #查看scores对象的尺寸
scores.shape #查看scores对象的数组形状
scores.dtype #查看scores对象的数据类型

"""
调用reshape()函数创建多维数组
ndarray对象的reshape()函数用于将一维数组转换为指定的多维数组
  ndarray.reshape(newshape,...)
其中newshape表示新数组的形状，newshape的类型为整数或者整数元组。
reshape()函数经常与arange()函数结合使用，生成任意n维数组。
"""
num=np.arange(0,24,1) #创建0到23的步长为1的一维数组
num_reshape=num.reshape((2,3,4))
print(num_reshape)
"""
NumPy中的zeros()函数用于生成指定形状的全0数组
numpy.zeros(shape,…)
shape表示新的数组形状，shape的类型为整数或者整数元组

和zeros函数一样使用方式的其他函数
ones 全是 1
eye  创建的是单位矩阵，也就是只有对角线有数字1其余为0
eye后面的参数表示的是 n行m列的列表
"""
num=np.zeros((3,2))
print(num)
num=np.ones((3,2))
print(num)
num=np.eye(3,3)
print(num)

"""
numpy中还有随机函数的调用
常见
numpy.random.rand(size)
随机产生一组[0,1)之间服从均匀分布的浮点值

numpy.random.randint(start,end,size)
随机产生一组[start,end)之间服从均匀分布的离散整数值

numpy.random.uniform(start,end,size)
随机产生一组[start,end)之间服从均匀分布的浮点值

numpy.random.normal(loe,scale,size)
随机产生一组给定均值 loe 和标准差 scale 的服从正态分布的浮点值
loe 对应着整个分布的中心
scale 对应着分布的密度
scale越大越矮胖，scale越小越瘦高
"""
arr1=np.random.rand(2,2)
print(arr1)
arr2=np.random.randint(0,10,(2,3))
print(arr2)
arr3=np.random.uniform(1,2,(3,4))
print(arr3)
arr4=np.random.normal(0,1,(2,3))
print(arr4)

persons=np.array(['宋江','吴用','林冲','秦明'])

# 数组元素的访问
"""
第一种使用索引方式查询
可以一次访问一个数值，也可以一次访问多个数值
"""
print(persons)
print(persons[2])    #取索引值为2的元素，得到字符串对象
print(persons[[0,2]])  #取索引值为0和2的元素，得到数组对象

print(scores)   #显示scores对象
print(scores[1,0])   #取索引值为（1，0）的数组元素
print(scores[[0],[0,2]])  #取索引值为（0，0），（0，2）的数组元素，返回数组
print(scores[[0,1],[0,2]])  #取索引值为（0，0），（1，2）的数组元素，返回数组

"""
还可以通过切片的方式进行查询
"""
print(persons)
print(persons[2:])
print(persons[1:3])

print(scores)
print(scores[1:,1:])
print(scores[:,1:3])
print(scores[:,[0,2]])

"""
还可以使用布尔运算进行筛选
"""

print(scores)
# 筛选分数段的方法
mask = ((scores>90)|(scores<80))
print(mask)
print(scores[mask])
