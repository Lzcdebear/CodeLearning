def IsProfNum(num):
    lst = []
    for x in range(1,num):
        if num % x == 0:
            lst.append(x)
    if sum(lst) == num :
        return True
    return False

proflst = []
for n in range(1,1000):
    if IsProfNum(n) == True:
        proflst.append(n)

print ('1000以内的所有完全数有：', proflst)