#John,1,2 Lucy,3,6 Nancy,3,6,9
#豆豆,5 小胖,2,7,9 八戒,0
uList=input('请在下方输入空格隔开的多人记录花销（逗号隔开的每人姓名和花销）：\n').split(' ') #每个人一个字符串组成的列表
#print(uList)

namelist = []
moneylist = []
for txt in uList:
    #print(txt)
    lst = txt.split(',')
    #print(lst)
    name = lst[0]
    m_lst = lst[1:]
    m_lst = [int(x) for x in m_lst] 
    #print(m_lst)
    money = sum(m_lst)
    namelist.append(name)
    moneylist.append(money)
#print(namelist)
#print(moneylist)
avg = sum(moneylist) / len(moneylist)
chae_lst = [x - avg for x in moneylist]
#print(chae_lst)
print(f"人均消费：{avg:.2f}元")
print(f"每人补差：")
for i in range(len(namelist)):
    name = namelist[i]
    chae = chae_lst[i]
    print(f'{name}\t{chae:+8.2f}')
    