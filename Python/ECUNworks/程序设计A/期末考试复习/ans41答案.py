'''
#John,1,2 Lucy,3,6 Nancy,3,6,9
#豆豆,5 小胖,2,7,9 八戒,0
uList=input('请在下方输入空格隔开的多人记录花销（逗号隔开的每人姓名和花销）：\n').split(' ') #每个人一个字符串组成的列表
'''

#参考答案2
#John,1,2 Lucy,3,6 Nancy,3,6,9
#豆豆,5 小胖,2,7,9 八戒,0
#豆豆,5 小胖,2,7,9 长脚,8,12 八戒,0
#John,1,2 Lucy,3,6 Nancy,3,6,9 豆豆,5 小胖,2,7,9 长脚兄,8,12 八戒,0
# uList=input('空格隔开的多人记录花销（逗号隔开的每人姓名和花销）：').split(' ') #每人单字符串列表
uList=[x.split(',') for x in input('请在下方输入空格隔开的多人记录花销（逗号隔开的每人姓名和花销）：\n').split(' ')] #每个人多字符串二维列表
sumTotal=0
for u in uList:
    sumPerson=0
    for i in u[1:]:
        sumPerson+=int(i)
    sumTotal+=sumPerson
    u.append(sumPerson)
avg=sumTotal/len(uList)
print('人均消费：%.2f元\n每人补差：'%avg)
for u in uList:
    print("%s\t%+8.2f"%(u[0],u[-1]-avg))
