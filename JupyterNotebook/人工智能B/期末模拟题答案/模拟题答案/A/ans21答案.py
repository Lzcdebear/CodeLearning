#fillblank_1.py 
#给定代码不准删除修改，所有填空使用一个表达式完成。
#评分标准：每空2分

import numpy as np
np.random.seed(6)  ##设定随机种子，不要改动！

#生成成绩：随机整数，范围在[40,100)之间,二维数组，每行数据依次为某同学的语文、数学、英语这三门课的成绩
scores=np.random.randint(40,100,(50,3)) #(1)
#请输入分数：
score=int(input("请输入分数："))

#统计输入分数以下的成绩信息：
mask=scores<score

#分别统计语文、数学、英语三门课在分数段以下的人数
print("语文、数学、英语三门课在{}分以下的人数分别为：".format(score),mask.sum(axis=0)) #(2)

#统计三门课都及格的人数
print("三门课都在{}分以上的人数为：".format(score),sum(mask.sum(axis=1)==0))  #(3)

#输出三门课的平均分
print("三门课的平均分分别为：",scores.mean(axis=0))#(4)

#输出三门课平均分在输入成绩以上的人数
print("三门课平均分在{}分以上的人数为：".format(score),sum(scores.mean(axis=1)>score))  #(5)
