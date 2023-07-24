# 集合的数学操作
# 第一个操作是交集操作，即求相同操作
# 可以使用字符串的 intersection 或者直接使用 & 来进行交集操作
s1 = {10, 20, 30, 40, 50, 60}
s2 = {30, 40, 50, 60, 70}
print(s1.intersection(s2))
print(s1 & s2)
# 第二种是并集操作，即求所有元素操作
# 可以使用 union 或者直接使用 | 进行并集操作
print(s1.union(s2))
print(s1 | s2)
# 第三种就是差集操作，即求两个集合之间某个集合独有的部分
# 可以使用 difference 或者直接使用 - 进行差集操作
print(s1.difference(s2))
print(s1 - s2)
# 第四种是对称差集，就是两个集合中所有元素中去除相同的元素，即求并集后去除交集
# 可以使用 symmetric_difference 或者 ^ 进行对称差集的操作
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
