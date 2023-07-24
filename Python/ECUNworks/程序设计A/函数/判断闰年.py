def isLeapyear(n):
    n = int(n)
    bol = False
    if n % 4 == 0 and n % 100 != 0:
        bol = True
    elif n % 400 == 0:
        bol = True
    return bol


a = input()
jug = isLeapyear(a)
if jug:
    print(a, '是闰年', sep='')
else:
    print(a, '不是闰年', sep='')
