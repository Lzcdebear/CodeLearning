shopInfo = "12号店 48528 23号店 56380 18号店 32854 4号店 68385 53号店 92383 6号店 28387 37号店 40238 8号店 70823"
b = 0
rew = [0 for i in range(8)]
lst = str.split(shopInfo)
clt = [lst[i:i+2:] for i in range(0, 16, 2)]
for i in range(8):
    clt[i][1] = int(clt[i][1])
print('各店利润：', clt)
for i in range(8):
    a = int(clt[i][1])
    b = b + a
ave = b / 8
print('平均利润为：', ave, sep='')
for i in range(8):
    a = int(clt[i][1])
    c = (a - ave)
    if c >= 0:
        rew[i] = c * 0.08
    else:
        rew[i] = 0
for i in range(8):
    name = str(clt[i][0])
    if rew[i] != 0:
        print(name, '奖金：', rew[i], sep='')
