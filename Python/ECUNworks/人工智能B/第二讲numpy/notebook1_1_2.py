# coding=utf-8
"""
对于单个数字和数组的计算，会将数字进行扩展，也就是广播机制
"""
from statistics import mean
import numpy as np
scores=np.array([[96,73,78],[90,89,92],[60,70,83]])
print(scores,'\n')
scores=scores+2
print(scores,'\n')
"""
对于多维数组和一维数组相加，要求列的数量一样，会自动将一维数组扩展行为多维数组 
"""
a=np.ones((2,5)) #创建2行5列的全1二维数组
print(a,'\n')
b=np.arange(1,6,1) #创建数值为1到5的一维数组
print(b,'\n')
c=a+b
print(c,'\n')
"""
一些可以使用的函数
abs fabs    计算各元素的绝对值
sqrt        计算各元素的平方根
square      计算各元素的平方
exp         计算各元素的指数
log log10   计算各元素的自然对数
sign        计算各元素的正负号
ceil        计算各元素的大于等于该元素的最小整数
floor       计算各元素的小于等于该元素的最小整数
cos sin tan 三角函数
mod         求模函数
equal
not_equal   比较两个数组对应元素是否相等，返回布尔数组
astype      转换数据类型
"""
arr1 = np.array([1.1, 2.8, 3.3, 4.4, 5.3221])
arr2= arr1.astype('int32')
print(arr2)

"""
sum             求和
mean            求算数平方根
min max         求最大值和最小值
argmin argmax   求最大值和最小值的索引

这些函数都有方向，如果不指定方向，则对所有元素统计
一维数组只有一个轴 0
二维数组有两个轴    行方向 1
                    列方向 0
方向确定使用 axis
"""
arr1=np.random.randint(1,100,(3,4))
print(arr1)
print(arr1.max())
print(arr1.argmax())
print(arr1.max(axis=1))
print(arr1.max(axis=0))


