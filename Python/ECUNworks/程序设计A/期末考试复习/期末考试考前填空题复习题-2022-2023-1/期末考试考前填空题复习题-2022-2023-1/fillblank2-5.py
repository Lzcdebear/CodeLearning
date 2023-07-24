def IsRoseNum(num):
    sNum = str(num)
    if len(sNum)!=4:return ________
    summ = 0
    for x in sNum:
        summ += int(x) _____ 4
    if summ == num :
        _______________
    return False

result = []
for n in range(0,10000):
    if __________:
        result.append(_____)
print ('10000以内的所有玫瑰花数有：', result)
