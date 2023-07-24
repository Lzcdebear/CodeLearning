# coding=utf-8
import pandas as pd
import numpy as np

'''
创建如图所示的表格对象phone。行序号从1~5。列标签是"公司","第一季度","第二季度","第三季度","第四季度"，一共5条记录。

季度 公司 第一季度 第二季度 第三季度 第四季度 
Apple 51.9 57.9 48.7 50.4 
Samsung 69.7 64.6 41.7 51.7 
Huawei 31.7 58.6 59.2 47.9 
Mi 41.7 38.6 58.0 58.9 
OPPO 69.8 31.1 58.7 30.4
'''
#方法一 使用列表创建
title = ["公司","第一季度","第二季度","第三季度","第四季度"]
recs = [["Apple",51.9,57.9,48.7,50.4],["Samsung",69.7,64.6,41.7,51.7],["Huawei",31.7,58.6,59.2,47.9],["Mi",41.7,38.6,58.0,58.9],["OPPO",69.8,31.1,58.7,30.4]]
phone = pd.DataFrame(recs, title)
print(phone)  
print('-----------------------------------------------')


#方法二 使用字典创建
title = ["公司","第一季度","第二季度","第三季度","第四季度"]
gs = ["Apple","Samsung","Huawei","Mi","OPPO"]
s1 = [51.9,69.7,31.7,41.7,69.8]
s2 = [57.9,64.6,58.6,38.6,31.1]
s3 = [48.7,41.7,59.2,58.0,58.7]
s4 = [50.4,51.7,47.9,58.9,30.4]
d = dict(zip(title,[gs,s1,s2,s3,s4]))
phone = pd.DataFrame(d)
print(phone.T)
print('-----------------------------------------------')


# (2)选择Huawei和Mi的第四季度数据增加10%
phone.loc[2,'第四季度'] = phone.loc[2,'第四季度'] * (1.1)
phone.loc[3,'第四季度'] = phone.loc[3,'第四季度'] * (1.1)
print(phone)
print('-----------------------------------------------')


# (3)所有Samsung的数据降低5%
phone.iloc[1,1:5] = phone.iloc[1,1:5] * 0.95
print(phone)
print('-----------------------------------------------')


# (4)分别统计五个公司在2019年的手机出货总量
print(phone.iloc[0,1:5].sum(), phone.iloc[1,1:5].sum(),phone.iloc[2,1:5].sum(),phone.iloc[3,1:5].sum(),phone.iloc[4,1:5].sum())

# (5)统计所有公司第一季度的手机总出货量和第四季度的手机总出货
print(phone['第一季度'].sum(), phone['第四季度'].sum())


# (6)找出每个季度出货量最大的公司(不是编号)
maxcom = []
maxnum = np.argmax(np.array(phone.iloc[:,1:5]),axis=0)
for i in maxnum:
    maxcom.append(phone.iloc[i,0])
print(maxcom)



# 第二大题
df = pd.read_csv(r"F:\Python\ECUNworks\人工智能B\第三讲pandas\EMSI_JobChange_UK.csv")
print(df)


#（2）查询London市的SIC Code、Jobs 2011和Jobs 2014三列数据。
print(df.loc[df['City']=='London',['SIC Code','Jobs 2011','Jobs 2014']])


#（3）添加两列："Change"列= Jobs 2014- Jobs 2011，"Change%"列=Change/ Jobs 2011。
df['Change'] = df.loc[:,'Jobs 2014'] - df.loc[:,'Jobs 2011']
df['Change%'] = df.loc[:,'Change'] / df.loc[:,'Jobs 2011']
print(df)


#（4）删除Country列
df.drop(["Country"],axis = 1,inplace = True) 
print(df)

#（5）查询教育行业（SIC Code:P）的城市就业情况，显示City 、Jobs 2011 、Jobs 2014 、 Change的数据，并按Change列由大到小排列
print(df.loc[df['SIC Code']=='P',["City","Jobs 2011","Jobs 2014","Change"]].sort_values(["Change"],ascending=False))
