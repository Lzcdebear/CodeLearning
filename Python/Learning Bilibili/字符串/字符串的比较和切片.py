"""
字符串的比较可以使用
> >= < <= == !=
比较规则：
首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，依次比较下去，直到两个字符串中的字符不相等，后续字符不再被比较

比较原理：
两个字符进行比较时，比较的是其 ordinal value
调用内置函数 ord 可以得到指定字符的 ordinal value
内置函数 ord 对应的就是内置函数 chr
调用内置函数 chr 时指定 ordinal value 可以得到对应字符

这里注意
== 比较的是两者的 value
is 比较的是两者的 id
"""
a = b = 'python'
c = 'python'
print(a == b)
print(a is b)
print(c == a)
print(c is a)
# 这里的 is 和 == 是因为
print(id(a))
print(id(c))
print(id(b))
"""
python的切片操作和列表一样
但是python是不可改变的序列，所以切片将会产生新的两个字符串，存放的id也不一样的，消耗内存
"""
s = 'python,nik'
s1 = s[:5]
s2 = s[6:]
s3 = ','
new = s1 + s3 + s2
print(new)
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(new))
