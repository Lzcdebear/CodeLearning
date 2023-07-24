"""

按照下列要求，设计完成一个程序。
a.	程序功能：编程请输出2-10之间的数字，其中如是合数，则显示为其两个因子乘积的形式，如是质数，则显示它是一个质数。
b.	程序运行结果如下图所示：
运行结果如下：

2 是一个质数
3 是一个质数
4等于2*2
5 是一个质数
6等于2*3
7 是一个质数
8等于2*4
9等于3*3
10等于2*5

"""
def is_prime(x):
    if x % 1 != 0:
        print('不是整数')
    for i in range(2,x):
        if x % i == 0:
            return False
        else:
            continue
    return True

b = 0  # 这是存储合数的其中一个因子的量
c = 0
jug = bool  # 这是存储是否为合数的量
for i in range(2, 11):
    jug = is_prime(i)
    if jug == True:
        print(i, ' 是一个质数', sep='')
    else:
        for j in range(2, i):
            if i % j == 0:
                b = j
                c = int(i / b)
                print(i, '等于', b, '*', c, sep='')
                break
