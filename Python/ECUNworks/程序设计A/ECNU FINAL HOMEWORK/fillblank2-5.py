def IsRoseNum(num):
    sNum = str(num)
    if len(sNum)!=4:return False
    summ = 0
    for x in sNum:
        summ += int(x) ** 4
    if summ == num :
        return True
    return False

result = []
for n in range(0,10000):
    if IsRoseNum(n)==True:
        result.append(n)
print ('10000以内的所有玫瑰花数有：', result)
