# 程序模板
x = int(input(''))
if x > 10 or x < -10:
    print("ERROR")
else:
    if x < 0:
        y = 2 * x * x * x + 4 * x * x + 3
        print(y)
    elif x < 6:
        y = x + 14
        print(y)
    elif x <= 10:
        y = 6 * x
        print(y)
