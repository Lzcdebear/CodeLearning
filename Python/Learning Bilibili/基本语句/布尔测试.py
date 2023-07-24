# 这里将会测试各种不同类型对象背后的布尔值方便展示
# 首先是布尔值是False的类型
print(bool(False))
print(bool(0))
print(bool(0.0))  # 数值为0的布尔值都是False
print(bool(''))
print(bool(""))
print(bool(' '))
print(bool(" "))
# 这里显示的是空字符串布尔值是False，但是注意如果中间加入空格，则不是空字符串，结果将会是True
print(bool(None))
# none de bool is False
print(bool([]))
print(bool(list()))
# 这里展示的是空列表的布尔值也是False
print(bool(()))
print(bool(tuple()))
# 这里展示的是空元组的布尔值也是False
print(bool({}))
print(bool(dict()))
# 这里展示的是空字典的布尔值也是False
print(bool(set()))
# 这里展示的是空集合的布尔值也是False
# 除了以上的布尔值是False，其余的所有对象的布尔值都是True
