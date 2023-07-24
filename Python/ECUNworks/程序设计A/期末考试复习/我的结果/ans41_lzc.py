# John,1,2 Lucy,3,6 Nancy,3,6,9
# 豆豆,5 小胖,2,7,9 八戒,0
uList = input('请在下方输入空格隔开的多人记录花销（逗号隔开的每人姓名和花销）：\n').split(' ')  # 每个人一个字符串组成的列表
# print(uList)

name_expense = {}
name_need = {}
expense = 0
all_expense = 0
people_num = int(len(uList))

for i in uList:
    expense = 0
    lst = i.split(',')
    leg = len(lst)
    for x in range(1, leg):
        expense += int(lst[x])
    name_expense[lst[0]] = expense
# print(name_expense)

for i in name_expense:
    all_expense += int(name_expense[i])
print("人均消费：{:.2f}元".format(all_expense / people_num))
ave = float(all_expense / people_num)
for i in name_expense:
    name_need[i] = float(name_expense[i]) - ave
# print(name_need)

print("每人补差：")
for i in name_need:
    name_need[i] = '%.2f' % name_need[i]
    print(f'{i}\t{(float(name_need[i])):+8.2f}')
