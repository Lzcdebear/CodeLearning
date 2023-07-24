# coding=utf-8
import pandas as pd
import numpy as np


'''
创建一个存储了3名学生的3门课程成绩的DataFrame对象scores，值为成绩，行索引为学号，列索引为课程名（计算机、英语和体育）。
成绩和学号由NumPy的随机数组生成函数randint()产生
知成绩的范围为0-100，学号的范围为200151800-200151900。
对scores进行以下操作并同步进行打印：
		首先加入学号为200151909、三门课成绩分别为88、76和90的学生，
		然后删除所有体育成绩，
		接着将所有学生的英语成绩乘以0.8，
		最后筛选出计算机成绩为80分以上的学生。
		把最后的数据写入到Excel文件，命名为“Scores.xlsx”。
'''
# 程序设计思路和程序
'''
（1）DataFrame对象scores的创建¶
np.random.randint(start,end,size)可以生成一个包含随机元素的数组，
这些元素的取值范围为从start到end-1；size表达大小，可以是一个整数，定义一维数组的长度，也可以是一个元组，定义一个二维数组的形状。
通过调用DataFrame()函数、randint()函数和astype()函数完成对scores的创建。
'''
stu=np.random.randint(0,101,(3,3))
xh=np.random.randint(200151800,200151901,3).astype(str)
scores=pd.DataFrame(stu,index=xh,columns=['计算机','英语','体育'])
print(scores)

# scores中元素的增加，通过赋值的方法加入新的学号和成绩。
scores=scores.append(pd.DataFrame([[88,76,90]],index=['200151909'],columns=['计算机','英语','体育']))#加入新的学号和成绩
print(scores)

# scores中元素的删除：删除列索引值为'体育'的元素，调用drop()函数完成对scores中元素的删除。
scores=scores.drop('体育',axis=1) #删除列索引值为'体育'的元素
print(scores)

# scores中元素的修改：取出列索引值为'英语'的元素乘以0.8再赋值给列索引值为'英语'的元素。
scores['英语']=scores['英语']*0.8#将列索引值为'英语'的成绩乘以0.8
print(scores)

# scores中元素的查询：程序通过布尔表达式scores['计算机']>=80来筛选出计算机成绩大于等于80的学生。
print(scores[scores['计算机']>=80])  # 检索计算机成绩大于等于80的学生
scores = scores[scores['计算机']>=80]  # 筛选出计算机成绩大于等于80的学生

# 把scores写入到Excel文件：程序通过to_excel()函数来完成把数据写入Excel文件，得到的Scores.xlsx文件内容如图所示。
scores.to_excel(r'F:\Python\ECUNworks\人工智能B\第三讲pandas\homework4_2_2test.xlsx')  # 从DataFrame对象写入数据到Excel文件