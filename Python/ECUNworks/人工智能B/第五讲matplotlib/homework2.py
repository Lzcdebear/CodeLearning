# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib

'''
综合练习题
#读取studentInfo.xlsx文件，完成以下要求

（1）将5张表拼接为一个DataFrame对象（名称为stu），去除‘序号’列，并输出stu结果
'''
df2 = pd.read_excel(r"F:\Python\ECUNworks\人工智能B\第五讲matplotlib\studentsInfo.xlsx",sheet_name="Group2") #
df3 = pd.read_excel(r"F:\Python\ECUNworks\人工智能B\第五讲matplotlib\studentsInfo.xlsx",sheet_name="Group3") #
df4 = pd.read_excel(r"F:\Python\ECUNworks\人工智能B\第五讲matplotlib\studentsInfo.xlsx",sheet_name="Group4") #
df5 = pd.read_excel(r"F:\Python\ECUNworks\人工智能B\第五讲matplotlib\studentsInfo.xlsx",sheet_name="Group5") #
df1 = pd.read_excel(r"F:\Python\ECUNworks\人工智能B\第五讲matplotlib\studentsInfo.xlsx",sheet_name="Group1") #
stu=pd.concat([df1,df2,df3,df4,df5])  #拼接5张表
print(stu)
stu.drop('序号',axis=1,inplace=True)
print(stu)

'''
（2）去除完全重复的数据行,并设置行索引为1，2，3，......， 
提示： #df对象的行数是df.shape[0],列数是df.shape[1] #修改df对象的行列标签，df.column=['','','',....]，df.index=......
'''
stu.duplicated()  #查看重复项情况

stu.drop_duplicates(subset=None,keep='first',inplace=True)   #去除完全重复的数据行
stu.index=[i for i in range(1,int(stu.shape[0])+1)]   #设置行索引为1，2，3，......，行数可用stu.shape[0]获得
print(stu)

'''
（3）填充剩余缺失值：成绩按照平均分填充，年龄填充为20岁，体重和月生活费按照后一条记录的数据填充,年龄设置为整数
'''
blankplace = stu.isnull()  #查看缺失项情况，isnull()可返回布尔数组，缺失值对应True，其他为False
avgscore='%.1f' % float(stu.mean()['成绩'])  #计算成绩的平均分
stu.fillna(value={'成绩':avgscore,'年龄':20},inplace=True)  #成绩按照平均分填充，年龄填充为20岁(建议value部分用字典)

stu['年龄']=stu['年龄'].astype(int) #年龄设置为整数（int）
stu.fillna(method='bfill',axis=0,inplace=True)  #体重和月生活费按照后一条记录的数据填充
print(stu)

'''
(4）将同学数据按照“成绩”从大到小排序，分别统计优秀（≥90）的学生人数和不合格（<60）的学生人数。
'''
stu['成绩']=stu['成绩'].astype(float) #成绩设置为浮点型（FLOAT）
stu.sort_values(['成绩'],axis=0,ascending=True,inplace=True)  #将同学数据按照“成绩”从大到小排序
print(stu.tail(10))  #显示后10个记录

#统计成绩优秀（≥90）的学生人数
a=stu[stu['成绩']>=90]['成绩'].count()
#统计成绩不合格（<60）的学生人数
b=stu[stu['成绩']<60]['成绩'].count()
print(a)
print(b)

#分别计算优秀与不合格同学的平均课程兴趣度（“课程兴趣”列）
stuf = stu[stu['成绩']<60]
stug = stu[stu['成绩']>=90]
stufavescore = stuf.mean()['课程兴趣']
stugavescore = stug.mean()['课程兴趣']
print(stufavescore,stugavescore)

#计算全体同学成绩的平均分与平均课程兴趣度
allavescore = stu.mean()['成绩']
allavexq = stu.mean()['课程兴趣']
print(allavescore,allavexq)


#分别按省份分组计算月生活费的平均值
group=stu.groupby(by=["省份"])  #按省份分组
avgg=group['月生活费'].mean()  #计算按省份分组的月生活费的平均值
print(avgg)


# 画图

#使用plt直接画柱状图
fig = plt.figure(figsize=(15,5)) #设置画面大小
plt.rcParams['font.sans-serif']=['SimHei']#显示中文
plt.bar(np.arange(avgg.size), avgg, width=0.8,color='green',tick_label=avgg.index)   #画柱状图
plt.title('各省的平均月生活费') 
plt.xlabel('省份')
plt.ylabel('月生活费')
plt.xticks(rotation=30, ha='right')
plt.show()


#使用子图方式画图 
#提示：set_xticks，set_xticklabels函数是matplotlib.axes._subplots.AxesSubplot对象的方法，可以增加一个一行一列的子图获取。 
#fig, ax = plt.subplots(1,1) #ax.set_xticks(...) #设置条形图行数据 #ax.set_xticklabels(...) #设置条形图行标签
fig, ax = plt.subplots(1,1)
fig.set_size_inches(15,5) #设置画面大小
plt.rcParams['font.sans-serif']=['SimHei']#显示中文
ax.set_xticks(np.arange(avgg.size)) #设置条形图行数据
ax.set_xticklabels(avgg.index, rotation=30, ha='right') #设置条形图行标签
ax.set(title='各省的平均月生活费', xlabel='省份',ylabel='月生活费') 
ax.bar(np.arange(avgg.size), avgg, color='green')  #画柱状图
plt.show() 

# 8 绘制散点图显示学生身高和体重之间的关系
heights=stu["身高"]
weights=stu["体重"]
plt.scatter(heights,weights,marker=".",label='散点图')  #画散点图
plt.title("体重身高散点图")
plt.show()


# 9 画出学生的课程兴趣分布饼图（即不同课程兴趣度的人数分布）
group=stu.groupby(by=["课程兴趣"])
kcxq=group["课程兴趣"].count() #得到不同课程兴趣度的人数分布，kcxq是个Series对象

plt.axis('equal')
plt.pie(kcxq,autopct='%d',pctdistance=1.1,startangle = 0, textprops=dict(color="black")) #画饼图
plt.legend( kcxq.index, title='课程兴趣', bbox_to_anchor=(-0.15, 0.8),\
                 fontsize='xx-small', loc="center left")
plt.show()