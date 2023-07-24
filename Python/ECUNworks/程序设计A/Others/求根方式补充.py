# 第一种引用math模组
import math
import cmath

a = float(input('Enter a number'))
b = math.sqrt(a)
print(b)
print(type(b))
# 第二种直接使用自带的pow函数
# pow的含义就是power，就是指代指数运算
c = pow(a, 0.3)
print(c)
print(type(c))
# 第三种引用math.cmath函数中的sqrt，它不仅可以计算得出实数，还可以用来解出虚数根
d = cmath.sqrt(a)
print(a)
print(type(a))
# 这里再来展示一下虚数根求法
a = float(input('Enter a number < 0'))
b = cmath.sqrt(a)
print(b)
print(type(b))
# 第四种方式是运用numpy模组
