'''
（1）请定义student类，
包含三个属性：stu_no（学号）、math（数学成绩）和chinese（语文成绩）
有对应的getStuNo()、getMath()和getChinese()方法获取对应的属性并返回；
有一个构造方法用于从外界接收三个参数并设置到三个属性中；
另外还有一个avg_score()方法计算该学生语文、数学两门课的平均分（保留1位小数）并返回。
'''

# 定义Student类
class Student:
    # 初始化学生
    def __init__(self,no,math,chinese):
        self.no = no
        self.math = math
        self.chinese = chinese
    # 获取信息方法函数
    def getStuNo(self):
        return self.no
    def getMath(self):
        return self.math
    def getChinese(self):
        return self.chinese
    # 获取语文数学平均分函数
    def avg_score(self):
        ave = (float(self.math) + float(self.chinese))/2
        return float(ave)
    
import numpy as np
import pandas as pd
df=pd.read_csv(r'F:\OneDrive\Coding\Python\ECUNworks\人工智能B\第十一讲面向对象\stu_score.txt',sep=' ',encoding='UTF-8')  ###
print(df)

stu_list=[]
num=df.shape[0]  #学生人数
L1=np.array(df['学号'].values)
L2=np.array(df['数学成绩'].values)
L3=np.array(df['语文成绩'].values)
for i in range(0,num):
    stu1 = Student(L1[i],L2[i],L3[i])
    stu_list.append(stu1)
print(stu_list)
#构造student类并加入列表stu_list
###
for i in range(0,num):
    stu2 = stu_list[i]
    if float(stu2.avg_score()) >= 90:
        print(f'学号：{stu2.no}，数学成绩：{stu2.math}，语文成绩：{stu2.chinese}')
    else:
        pass
    