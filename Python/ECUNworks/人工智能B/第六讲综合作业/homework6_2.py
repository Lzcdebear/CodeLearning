# coding=utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 绘制某家庭年各项消费占比的饼图
#设置中文显示和字体
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['font.size'] = 16
#设置画布尺寸为12*12英寸
plt.figure(figsize=(12, 12))  # 设置画布尺寸12*12英寸
#准备数据
Items = ['教育', '食品', '服装', '旅游', '保险', '其它']  # 定义饼图的标签
explode = [0.1, 0.01, 0.01, 0.01, 0.01, 0.01]  # 设定各项距离圆心距离
Expenses = [30000, 12000, 8000, 24000, 3500, 8000]
#绘制饼图
plt.pie(Expenses, explode=explode, labels=Items, autopct='%4.2f%%', shadow=True)  # 绘制饼图
plt.title('家庭年各项消费比较表')  #设置标题
plt.legend(Items, loc=(12/12,6/12))  #设置图例
plt.show()


# 绘制散点图
#读取CSV文件Iris_plot.csv的数据到DataFrame
data = pd.read_csv(r'F:\Python\ECUNworks\人工智能B\第六讲综合作业\Iris_plot.csv') #
print(data)

#准备数据
X = data['petal_length']  #准备x轴数据
Y = data['petal_width']   #准备y轴数据
#设置画布大小为12*10英寸
fig = plt.figure(figsize=(12,12))  #
#绘制散点图
plt.scatter(X[:50], Y[:50], color='green', marker='o', label='setosa')  # 前50个样本
plt.scatter(X[50:100], Y[50:100], color='blue', marker='x', label='versicolor')  # 中间50个
plt.scatter(X[100:],Y[100:], color='red', marker='+', label='Virginica')  # 后50个样本
plt.legend(loc=2)  # 图例显示在左上角
plt.grid()
plt.show()

#绘制箱型图
#设置图元参数
plt.rcParams['font.sans-serif'] = ['SimHei']  # 避免中文出现乱码
plt.rcParams['axes.unicode_minus'] = False
#准备数据
#随机产生一组取值为[50,90)之间,size值为(10,12)的整数，模拟上海市一年的平均相对湿度百分比
humidity = np.random.randint(50,90,(10,12))
#设置标签
labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
#绘制箱型图
plt.boxplot(humidity, labels=labels, sym='*', whis=1.25, widths=0.6) #绘制箱型图
plt.xlabel('平均相对湿度百分比')  #设置x轴标签 
plt.show()


