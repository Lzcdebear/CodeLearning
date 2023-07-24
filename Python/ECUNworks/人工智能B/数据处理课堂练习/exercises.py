import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# L = [62,86,59,75,38,9,75,97,90,57,74,33,50,57,32,89,90,96,51,82]
# data=np.array(L) 	#将列表数据L转成数组data
# score=int(input("请输入查询分数：\n"))
# ##筛选数组中成绩大于等于所查询分数的数据
# mask= score
# result=data[data>=mask]
# ##利用ndarray对象属性求数组元素个数
# count=result.size
# print ("成绩大于等于{}的数据有{}个，具体是:{}".format(score,count,result))

'''
2.利用随机函数模拟果汁生产线上每瓶饮料的实际装瓶容量。饮料装瓶核定容量为300ml，
实际装瓶容量的标准差为5ml（服从均值为300、标准差为5的正态分布）。
假设抽检5个批次，每次8瓶果汁样品。
(1)生成5*8的数组保存每瓶的实际容量并显示；
(2)输出每个批次装瓶容量的实际均值（输出小数位限制为2位）；
(3)找出装瓶容量最少的批次和容量。
'''
# np.random.seed(int(input()) )
# #设置显示精度为两位小数
# np.set_printoptions(precision=2, suppress=True)
# #按照正态分布(均值300，标准差50)随机生成5*8的数组模拟装瓶容量，并输出
# sample = np.random.normal(300,5,(5,8))
# print ("1. \n", sample)
# #输出每个批次装瓶容量的实际均值
# samplemean = sample.mean(axis=0)
# print("2. \n", samplemean)  
# #找出装瓶容量最少的批次并输出。
# print("3.\n",f"装瓶容量最少是第{int(np.argmin(samplemean))+1}批，容量为{float(samplemean[np.argmin(samplemean)]):.2f}ml" ) 

'''
程序功能：根据字典对象data创建dataFrame对象df，完成以下操作：
（1）使用'temperature'列的最大值填充'temperature'列的缺失值。
（2）增加一行["Sun.",8]。
（3）将'temperature'列数据增加5%。
（4）输出"temperature"列大于10的数据。
'''
# data = {"weekday":["Mon.","Tues."," Wed.","Thur.","Fri.","Sat."],\
#         "temperature":[ 9,16,np.nan,14,11,5]}
# df=pd.DataFrame(data)
# df['temperature'].fillna(df["temperature"].max(),inplace=True)
# df=df.append({'weekday':"Sun",'temperature':8},ignore_index=True)
# df['temperature']=df['temperature'] * (1+0.05)
# print(df[df["temperature"]>10])

'''
程序功能：文件jumpracedata.csv存放着某次比赛中7位选手的跳高成绩，每列为一个轮次，除第1行为轮次序号外，其余各行分别对应各位选手的跳高成绩（单位为cm），共有4轮比赛。 编程实现一下功能:
（1）读入jumpracedata.csv，生成DataFrame对象。
（2）列表s5是第5轮的成绩，添加到df对象中。
（3）增加一列"最好成绩",值为每一个运动的最好成绩。
（4）最好成绩大于等于150cm的队员出线，输出出线的运动员和最好成绩（分两列）。
'''
# s5=[142,111,82,90,176,125,93]
# #读入jumpracedata.csv，生成DataFrame对象
# df = pd.read_csv(r"F:\OneDrive\Coding\Python\ECUNworks\人工智能B\数据处理课堂练习\jumpracedata.csv",encoding="gbk")
# #将第5轮成绩（列表s5），添加到df对象中
# df['第五轮']=s5
# #增加一列"最好成绩",值为每一个运动的最好成绩
# df["最好成绩"]=df.max(axis=1)
# print(df)
# #最好成绩大于等于150cm的队员出线，输出出线的运动员和最好成绩（分两列）
# print(df[df['最好成绩']>=150][['运动员','最好成绩']])

'''
程序功能：读取文件数据，按要求绘制图形。具体说明和要求如下：
（1）文件sales.xlsx中存放着某些商品的销售情况（含有“商品名”、“单价”和“销售量”3列数据）。
读入sales.xlsx数据，生成DataFrame对象 。
（2）根据商品的销售金额（=单价 * 销售量），使用matplotlib.pyplot 模块画出如下图所示的条形图
（3）图形的 x 轴标签为“商品名”，y 轴标签为“'销售金额（元）”，标题为“某地区部分商品销售金额”，
条型宽度为0.5、绿色，将图形以文件名fig2.png保存在当前目录。
'''
# #设置图像字体为SimHei
# plt.rcParams['font.sans-serif'] = ['SimHei']  
# plt.rcParams['axes.unicode_minus'] = False
# #读入Excel文件sales.xlsx
# df=pd.read_excel(r"F:\OneDrive\Coding\Python\ECUNworks\人工智能B\数据处理课堂练习\sales.xlsx")
# #取商品名列
# product=  df['商品名']
# #计算商品的销售金额（=单价 * 销售量）
# totalprice = df['单价'] * df['销售量']
# print(totalprice)
# print(product)
# plt.title('某地区部分商品销售金额')
# #绘制柱形图
# plt.bar(product,totalprice,tick_label=product.values,width=0.5,color="g")
# plt.xlabel("商品名")
# plt.ylabel('销售金额（元）')
# #将图形以文件名fig2.png保存在当前目录
# plt.savefig("fig2.png")
# plt.show()

'''
程序功能：读取文件数据，按要求绘制图形。具体说明和要求如下：
（1）文件trip.csv中存放着两位行者的日行走距离数据（列"行者A" 和列"行者B"分别表示在列“日期”的某段时间内他们每天行走的距离m） 。
读入trip.csv数据，生成DataFrame对象。
（2）从DataFrame对象中提取列"行者A"、"行者B"和“日期”数据，使用matplotlib.pyplot模块画出如下图所示的折线图。
（3）图形的 x 轴标签为“日期”，y 轴标签为“行走距离（m）”，标题为“两行者行走距离折线图”，并绘制网格线，
将图形以文件名fig2.png保存在当前目录。
'''
df = pd.read_csv(r'F:\OneDrive\Coding\Python\ECUNworks\人工智能B\数据处理课堂练习\trip.csv')
dataA = df['行者A']
dataB = df['行者B']
dataday = df['日期']
plt.plot(dataday,dataA,color='b')
plt.plot(dataday,dataB,color='r',linestyle='--')
plt.xlabel='日期'
plt.ylabel='行走距离(m)'
plt.show()