'''公司某一地区连锁门店一个月的利润已保存在字符串shopInfo中，需将各门店以及该门店的利润组成
 #[[店名1,利润]1,[店名2,利润2],[店名3,利润3],...]的二维列表并输出，同时计算输出平均利润，
 #为利润超过平均值的门店提供奖励，奖金是超过平均值部分的8%，计算输出得到奖金的门店名称以及所得奖金。
 #结果如下所示（保留2位小数）：
各店利润： [['12号店', 48528], ['23号店', 56380], ['18号店', 32854], ['4号店', 68385], ['53号店', 92383], ['6号店', 28387], ['37号店', 40238], ['8号店', 70823]]
平均利润为：54747.25
23号店奖金：130.62
4号店奖金：1091.02
53号店奖金：3010.86
8号店奖金：1286.06
'''
shopInfo="12号店 48528 23号店 56380 18号店 32854 4号店 68385 53号店 92383 6号店 28387 37号店 40238 8号店 70823"
shopInfo=shopInfo.split() #拆分字符串到列表
shopsCount=len(shopInfo)//2 #门店数量，保持整数

profit=[] #二维列表 [[店名1,利润]1,[店名2,利润2],[店名3,利润3],...]
for i in range(shopsCount): #
    profit.append([shopInfo[i*2],int(shopInfo[i*2+1])])
print("各店利润：",profit)

totalProfit=0 #总利润
for i in profit:
    totalProfit+=i[1]
avgProfit=totalProfit/shopsCount  #平均利润
print('平均利润为：%.2f'%avgProfit)

bonusPrec=0.08  #奖金比例
for i in profit:
    delta=i[1]-avgProfit
    if delta>0:
       print(f'{i[0]}奖金：{delta*bonusPrec:.2f}')