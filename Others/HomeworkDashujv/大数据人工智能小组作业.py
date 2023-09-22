import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei']
df1=pd.read_excel("F:\\OneDrive\\Coding\\Others\\HomeworkDashujv\\中国平安财报.xlsx")
df2=pd.read_excel("F:\\OneDrive\\Coding\\Others\\HomeworkDashujv\\中国人寿财报.xlsx")
df3=pd.read_excel("F:\\OneDrive\\Coding\\Others\\HomeworkDashujv\\中国太保财报.xlsx")
for i in range(5):
    df1.loc[i,"余额"]=df1.loc[:i,"收入"].sum()-df1.loc[:i,"支出"].sum()
for i in range(5):
    df2.loc[i,"余额"]=df2.loc[:i,"收入"].sum()-df2.loc[:i,"支出"].sum()
for i in range(5):
    df3.loc[i,"余额"]=df3.loc[:i,"收入"].sum()-df3.loc[:i,"支出"].sum()
fig=plt.figure(figsize=(8,4))
plt.subplot(1,1,1)
plt.plot(df1.日期,df1.余额)
plt.plot(df2.日期,df2.余额)
plt.plot(df3.日期,df3.余额)
plt.title("各大保险公司财报")
plt.xlabel("日期")
plt.ylabel("累计利润/（万元）")
plt.grid()
plt.legend(["中国平安","中国人寿","中国太保"])
plt.show()
