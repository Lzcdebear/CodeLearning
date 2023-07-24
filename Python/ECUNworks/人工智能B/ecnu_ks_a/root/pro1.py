#pro1.py
#导入相关包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False


stu_data_ori = pd.read_csv('F:\\OneDrive\\Coding\\Python\\ECUNworks\\人工智能B\\ecnu_ks_a\\root\\student_score.csv',sep='\t',encoding='gbk')
#（1）读取c:\ecnu_ks\root中的文件student_score.csv中的学生语文、数学、英语三列成绩数据,注意csv文件中的分隔符，且文件中含中文字符
#（2）数据清洗：清除三门课全部缺考的学生，将部分缺考的学生成绩设为0
#（3）数据统计和分析：输入一个总成绩，输出比这个总成绩高的人数。
#（4）绘制出数学成绩各成绩段的饼图并保存为"pie.png"。
# print(stu_data_ori)
stu_data = stu_data_ori.loc[:,['语文','数学','英语']]
stu_data[stu_data=='缺考']=np.nan
stu_data.dropna(how='all',inplace=False)
stu_data = stu_data.fillna(0)
req_Score = input('输入一个总成绩：')
stu_sum = stu_data.astype('int32').sum(axis=1)
print('比这个总成绩高的人数有{}位'.format(len(stu_sum[stu_sum>int(req_Score)])))

# 绘制数学成绩各成绩段的饼图并保存为"pie.png"
bins = [0, 59, 69, 79, 89, 100]  # 成绩段划分
labels = ['不及格', '60~70分', '70~80分', '80~90分', '90~100分']  # 成绩段标签
math_scores = stu_data['数学']
score_categories = pd.cut(math_scores.astype('int32'), bins=bins, labels=labels)
score_counts = score_categories.value_counts()
# 绘制饼图
plt.pie(score_counts, labels=labels, autopct='%1.1f%%')
plt.title("成绩分布")
plt.axis('equal')

# 保存饼图为"pie.png"
plt.savefig('F:\\OneDrive\\Coding\\Python\\ECUNworks\\人工智能B\\ecnu_ks_a\\root\\pie.png')

# 显示饼图
plt.show()
