#pro1.py
#导入相关包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False


#（1）读取c:\ecnu_ks\root中的文件student_score.csv中的学生语文、数学、英语三列成绩数据,注意csv文件中的分隔符，且文件中含中文字符
#（2）数据清洗：清除三门课全部缺考的学生，将部分缺考的学生成绩设为0
#（3）数据统计和分析：输入一个总成绩，输出比这个总成绩高的人数。
#（4）绘制出数学成绩各成绩段的饼图并保存为"pie.png"。
