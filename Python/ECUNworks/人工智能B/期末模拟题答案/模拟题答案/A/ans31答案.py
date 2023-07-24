#pro1.py
#评分标准：每个步骤5分，共20分
#导入相关包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False


#（1）读取c:\ecnu_ks\root中的文件student_score.csv中的学生语文、数学、英语三列成绩数据,注意csv文件中的分隔符，且文件中含中文字符
df=pd.read_csv("student_score.csv",sep="\t",encoding="gbk",usecols=["语文","数学","英语"])


#（2）数据清洗：清除三门课全部缺考的学生，将部分缺考的学生成绩设为0
mask=df=="缺考"
df[mask]=np.NaN
df.dropna(how="all",inplace=True)
df.fillna(0,inplace=True)

#(3)数据统计和分析：输入一个总成绩，输出比这个总成绩高的人数。
df=df.astype("int64")
ascore=int(input("输入一个总成绩："))
print("比这个总成绩高的人数有{}位。".format(sum(df.sum(axis=1)>ascore)))

#（4）绘制出数学成绩各成绩段的饼图并保存为"pie.png"。
a=sum(df.数学<60)
b=sum((df.数学>=60) & (df.数学<70))
c=sum((df.数学>=70) & (df.数学<80))
d=sum((df.数学>=80) & (df.数学<90))
e=sum((df.数学>=90) & (df.数学<=100))
labels = ['不及格','60~70分','70~80分','80~90分','90~100分']
sizes = [a,b,c,d,e] #各个值 (最重要的数据 )
plt.pie(sizes,labels=labels,autopct='%.1f%%') #饼内百分数格式
plt.title("成绩分布")
plt.savefig('pie.png')
plt.show()