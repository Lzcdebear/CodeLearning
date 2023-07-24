# 第一项展示int整数类型
n1 = 65
n2 = 68
print(n1, type(n1))
print(n2, type(n2))
# 除了十进制，还可以表示二进制八进制十六进制
# 接下来展示二进制表示为十进制的过程
print('二进制转化为十进制', 0b10110011)  # 二进制使用0b表示二进制数
print('八进制转化为十进制', 0o12564755)  # 八进制使用0o表示八进制数
print('十六进制转化为十进制', 0x1a2b3c4d5d5f5e)  # 十六进制使用0x表示十六进制
# 接下来展示浮点数，及其存储不太精确,可能会有误差可能没有误差
a1 = 1.1
a2 = 2.2
a3 = 2.1
print(a1, type(a1))
print(a1 + a2, a1 + a3)
# 展示利用模块将浮点数计算变得较为准确的方法
from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))
# 接下来是bool布尔数值，只有对与错两种值，分别可以作为1与0计算,输入的时候要首字母大写
f1 = True
f2 = False
print(f1, type(f1))
# 接下来展示布尔数据和整数的运算，直接进行计算即可
print(f1 + 1)
print(f2 + 1)
# 接下来是字符串类型，用''和""表示字符串必须在一行中显示
str1 = '编程为什么这么复杂呀！'
str2 = "编程为什么这么复杂呀！"
print(str1, type(str1))
print(str2, type(str2))
# 接下来展示’‘’ ‘’‘与“”“ ”“”字符串可以在连续几行中显示，其中所有的换行都将会显示
str3 = '''编程的要求


真是多'''
str4 = """编程的要求
真是多"""
print(str3, type(str3))
print(str4, type(str4))
# 接下来是数据类型转换，进行数据连接的时候只能将相同的数据类型进行连接
name = '王尼玛'
age = 18
print('my name is '+name+' I am '+str(age)+' years old')  # 将int类型转换为str类型
