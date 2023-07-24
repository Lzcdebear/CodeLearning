"""

 按照下列要求，完成计算组合的程序。
（1）  定义函数fact(n)，返回正整数n的阶乘。
（2）  输入两个正整数n和m ，要求这两个数之间用逗号间隔， 根据求组合公式C(n,m)=n!/((n-m)!m!)， 通过调用 函数fact(n)，输出每组n、m的组合C(n,m)。
（3）  程序运行结果示例：
请输入两个用逗号间隔的正整数：
3，2
C(3,2) = 3

"""

def fact(n):
    x = 1
    for i in range(1, n+1):
        x = x * i
    return x

l = input('请输入两个用逗号间隔的正整数：\n')
k = l.split(',')
a = int(k[0])
b = int(k[1])
t = a - b
t = fact(t)
p = fact(a)
q = fact(b)
w = int(p / (t * q))
print('C(', a, ',', b, ') = ', w, sep='')
