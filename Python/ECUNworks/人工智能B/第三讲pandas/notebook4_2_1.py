# coding=utf-8
from string import printable
import pandas as pd
import numpy as np

'''
创建对象 Series 
series索引默认是 0 - n-1
但是可以改变索引值
但是索引位置依旧是 0 - n-1
每个索引位置对应一个值
创建方式
pandas.Series(data, index=[])
data	是存储在值里的数据，可以是numpy的列表或者数组
index	是索引，使用列表
'''
ability=pd.Series([99,87,88,75],index=['宋江','吴用','林冲','秦明'])
print(ability)

'''
Series对象既可以类似序列，使用位置索引获取对应的元素；也可以类似字典，通过索引名获取对应的元素。
	Series对象[索引]
还可以通过布尔运算表达式查找满足条件的元素。
	Series对象[布尔表达式]
'''
print(ability['宋江'])  #使用index索引访问
print(ability[0])        #使用位置索引
print(ability[ability.values>=80])

'''
(2)Series中元素的增加和修改
  通过赋值语句能很方便地完成Series中元素的增加和修改，格式如下：

    Series对象[索引] = 值

  当索引值是已存在的，赋值语句完成修改操作；当索引值是不存在的，赋值语句完成增加操作
'''
ability['宋江']=95
print(ability)
ability['武松']=80
print(ability)


'''
(3)Series中元素的删除
调用pop()函数进行删除
	pop()函数用于从Series对象中弹出索引值对应的元素，
	删除索引值对应的元素，且返回被删除的元素值。pop()函数会修改原始对象，其常用格式如下：

    Series.pop(item)

  其中，item是将要被删除元素对应的索引值。

调用drop()函数进行删除
  drop()函数表示从Series中删除单个或多个索引值对应的元素，并返回删除元素后的Series，该函数在默认情况下不修改原始对象，其常用格式如下：

    Series.drop(labels,…)

  其中，labels可以是单个索引值也可以是多个索引值组成的列表。
'''
popvalue = ability.pop('林冲')
print(ability)
print(popvalue)
ability_new=ability.drop(['吴用','秦明'])
print(ability)
print(ability_new)

'''
series的综合运用
'''

'''
Series对象score的创建
  通过调用randint()函数随机生成学生成绩，
	randint()函数随机生成学号时调用astype()函数转化为字符串类型，最后调用Series()函数完成score的创建。
'''
fs=np.random.randint(0,101,5)
xh=np.random.randint(200151800,200151901,5).astype(str)
score=pd.Series(fs,xh)
print(score)

'''
（2）score中元素的增加
  通过赋值的方法加入新的学号和成绩。
'''
#（2）score中元素的增加
score['200151909']=88    #加入新的学号和成绩
print(score)

'''
（3）score中元素的删除
  删除新加入的学生，调用pop()函数完成对score中元素的删除。
'''
score.pop('200151909')    #将学号为200151909的成绩进行删除
print(score)

'''
（4）score中元素的修改
  Series对象的底层是NumPy库，同样支持整体运算，直接执行减法运算。
'''
score=score-5      #将所有成绩都减去5
print(score)

'''
（5）score中元素的查询
  程序通过布尔表达式score.values>=80来筛选出成绩大于等于80的学生。
'''
print(score[score.values>=80])    #检索成绩大于等于80的学生