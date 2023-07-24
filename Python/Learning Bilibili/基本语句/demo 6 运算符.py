# 算数运算符使
print(1 + 1)    # 加法运算符 +
print(1 - 1)    # 减法运算符 -
print(4 / 2)    # 除法运算符 /
print(4 * 2)    # 乘法运算符 *
print(11//2)    # 整除运算符 //
print(2 ** 2)   # 幂运算符 **
print(11 % 2)   # 取余运算符 %
# 取整运算中若是出现一整一负，即结果商是一个负数的时候，向下取整，即取比商小1的数字
print(9//2)     # 2
print(-9//-4)   # 2
print(-9//4)    # 本身为-2余-1，向下取整为-3
print(9//-4)    # 本身为-2余-1，向下取整为-3
# 取余运算中被除数和除数的正负会影响结果，遵循的原则是
# 余数 = 被除数 - 除数 * 商
print(9 % 4)    # 结果为1 ，1 = （9） - （4 * 2）
print(-9 % -4)  # 结果为-1，-1=（-9） -（-4 * -3）
print(-9 % 4)   # 结果为3 ，3 = （-9）- （4 * -3）
print(9 % -4)   # 结果为-3，-3= （9） -（-4 * -3）
# 赋值运算符
# 注意：赋值运算符是从右想左进行运算的
a = 4 / 2
print(a)
# python还支持链式赋值
a = b = c = 20
print(a, b, c)
print(id(a), id(b), id(c))
# 链式赋值运算将不同的函数连接上同一个数字
#
# python还支持参数赋值 += -= /= *= //=
a = 10
a += 10
print(a, type(a))
a = 10
a *= 10
print(a, type(a))
a = 10
a -= 10
print(a, type(a))
a = 10
a /= 10
print(a, type(a))
a = 10
a //= 10
print(a, type(a))
# python还支持解包赋值
# 即一一对应相应从右向左一一赋值
a, b, c, = 10, 20, 30
print(a, b, c)
# 可以用在快速交换几个变量的值
print(a, b)
a, b = b, a
print(a, b)
#
# 比较运算符
# 结果为bool值，True或者是False
print(a > b)
print(a < b)
print(a == b)
print(a is b)
print(a is not b)
#
# 布尔运算符
f1 = f3 = True
f2 = f4 = False
# and 两个结果都是True的时候才是True
print(f1 and f2)
print(f1 and f3)
print(f2 and f4)
# or  两个中至少有一个是True就是True
print(f1 or f2)
print(f1 or f3)
print(f2 or f4)
# not 将原来的布尔值取反，True变成False，而False变成True
print(not f1)
print(not f2)
# in / not in 查看对象是否在其中,查找字符串或者是其他的东西
a = '老子就是老子'
b = 'old is old'
print('老子' in a)
print('o' in a)
print('老子' in b)
print('o' in b)
#
# 位运算符
print(4 & 8)   # & 位与运算只有全都是1时候才是1，其余情况都是0（二进制代码中）
print(4 | 8)   # | 位或运算只有全都是0时候才是0，其余情况都是1（二进制代码中）
print(4 << 1)  # << 向左移动一位，数字情况就相当于乘以多少个2
print(4 >> 1)  # >> 向右移动一位，数字情况就相当于除以多少个2
