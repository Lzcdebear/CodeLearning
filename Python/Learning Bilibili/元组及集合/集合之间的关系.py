# 两个集合之间是否相等
s1 = {10, 20, 30, 40}
s2 = {30, 20, 40, 10}
print(s1 == s2)
print(s1 != s2)
# 一个集合是否是另一个集合的子集
s1 = {10, 20, 30, 40, 50, 60, 70}
s2 = {10, 20, 30, 40, 50}
s3 = {10, 20}
print(s1.issubset(s2))
print(s3.issubset(s2))
# 一个集合是否是另一个集合的超集
print(s1.issuperset(s2))
print(s3.issuperset(s2))
# 两个集合是否没有交集
'''
没有交集为 True
如有交集为 False
'''
s4 = {10, 'jkl'}
s5 = {'jkl'}
print(s1.isdisjoint(s4))
print(s1.isdisjoint(s5))
