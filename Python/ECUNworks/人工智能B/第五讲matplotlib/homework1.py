# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib

'''
请画出下面函数曲线图，x区间取[0,2].增加合适的轴标签和图标题
提示：函数为 (𝑠𝑖𝑛(𝑥−2))2与𝑒−(𝑥2)之积，e的幂用np.exp()。x区间中点的个数可自定。
'''
# 准备数据
x = np.arange(0, 2, 0.01)  #准备[−π,2π]间隔0.01的数组
y = ((np.sin(x - 2)) ** 2) * (np.exp(-x ** 2))
# 添加画布内容
plt.title('$f(x)=sin^2(x-2)e^{-x^2}$') #图表标题
plt.xlabel('x')                         #x轴标题
plt.ylabel('y')                         #y轴标题
#绘制图形
plt.plot(x, y)                       #绘制曲线图
#绘制网格线
plt.savefig("homework1.png")              #保存图形文件
plt.show()                           #显示图形
