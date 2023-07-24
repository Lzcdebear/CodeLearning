"""
编程找出100-120之间所有的素数。
要求：定义判断一个数是否是素数的函数is_prime，参数是整数，如果这个数是素数则返回True，否则返回False
      循环，通过调用函数 is_prime得到100-200之间的所有素数，并输出，输入结果如下所示。
运行结果：

101是素数
103是素数
107是素数
109是素数
113是素数

"""


def is_prime(x):
    if x % 1 != 0:
        print('不是整数')
    for i in range(2, x):
        if x % i == 0:
            return False
        else:
            continue
    return True


for j in range(100, 121):
    a = is_prime(j)
    if a is True:
        print(j, '是素数', sep='')
    else:
        continue
