# 可以对列表中的元素添加、删除、修改或者排序
# 这里先展示添加
# 可以使用
"""
append 在列表末尾添加一个元素
extend 在列表末尾至少添加一个元素
insert 在列表的任意位置添加一个元素
切皮    在列表的任意位置至少添加一个元素
"""
# 在列表末尾添加一个元素
lst = [10, 20, 30]
print(id(lst))
lst.append(100)
print(lst)
print(id(lst))
# 这里表示的就是lst在添加前后占用的内存位置是一样的
# 接下来展示append和extend的区别
lst = [10, 20, 30]
lst2 = [50, 60, 90, 800]
lst.append(lst2)
print(lst)
lst = [10, 20, 30]
lst2 = [50, 60, 90, 800]
lst.extend(lst2)
print(lst)
# append只能添加一个元素，所以会把所有部分，即便是列表，也当作一个对象加入
# extend可以添加不止一个元素，所以可以把一个列表内的元素依次添加进去
# 而insert可以在任意位置添加元素。位置编号是由0开始
a = [10, 20, 30]
a.insert(2, 2365)
print(a)
a = [23123, 20, 30]
a.insert(2, 2365)
print(a)
a[1:] = lst
# 这个表达的意思就是把a切片到第二个，也就是保留第一个，然后将lst添加到a上面
'''
实际中的表现效果就是
例如前面的 a[23123, 10, 30]  lis[1, 2]
通过这样的表达的结果就是 a 最终变成 [23123, 1, 2]
这里的冒号后面可以添加数字，意思就是从前一个数字切片到后一个数字减一，这一部分不要，再加上后面的lis
'''
a = [1, 2, 3, 4, 5, 6]
lst = ['Nikolai is my husband']
a[0:4] = lst
print(a)
