#John,1,2 Lucy,3,6 Nancy,3,6,9
#豆豆,5 小胖,2,7,9 八戒,0

#John,1,2 Lucy,3,6 Nancy,3,6,9 豆豆,5 小胖,2,7,9 长脚兄,8,12 八戒,0

uList=input('请在下方输入空格隔开的多人记录花销（逗号隔开的每人姓名和花销）：\n').split(' ') #每个人一个字符串组成的列表
#print(uList)
uList = [x.split(',') for x in uList]
#print(uList)
money_lst = []
allmoney = 0
for item in uList:
    #['John', '1', '2']
    name = item[0]
    money = sum([int(x) for x in item[1:]])
    money_lst.append((name,money))
    allmoney = allmoney + money
print(money_lst)

avg =  allmoney/len(money_lst) 

print(f"人均消费：{avg:.2f}元")
print(f"每人补差：")
for name,money in money_lst:
    print(f'{name}\t{money - avg:+8.2f}')
