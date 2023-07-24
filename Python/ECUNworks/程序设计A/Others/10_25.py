# 打印倒三角符号
for i in range(12):
    for j in range(0, i):
        print(end=' ')
    for k in range(i, 12):
        print(end='*')
    print('\n')
# 输入三角形
a = int(input('请输入直角三角形包含的行数'))
i = 1
x = 1
n = a / 10  # 取整，有多少个十
m = 0
w = 0
'''
while m <= n:  # 判断要输出几次
    if a <= 10:
        while i <= a:  # 取遍 a 的所有值
            x = i % 10  # 取出 a 的个位数
            while x != 0:  # 循环 x 到 1
                print(x, end='')
                x -= 1
            while x == 0:
                while w <= m:
                    print('0', end='')
                    print(987654321)
                    w += 1
            print('\n')
            i += 1
    m += 1
'''
str1 = ''
o = a % 10
while n >= 0:
    while o >= 0:
        str2 = str(o)
        o -= 1
