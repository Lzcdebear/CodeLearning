# 对于列表的排序可以使用 sort 默认按照从小到大的顺序，但是可以使用指定 reverse = True 来进行倒序排序
# 也可以使用 sorted 使用 reverse = True 来进行降序排序, 如果没有 reverse 限定，则会默认为升序排列
lst = [10, 648, 256, 20, 40, 30]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
# 这里注意，sort是对列表进行操作，是lst后面加上 .
# 但是sorted是内置的函数，输入是lst，会重新输出一个列表
lst = [90, 50, 60, 87, 123, 110]
lst_new = sorted(lst, reverse=True)
print(lst_new)
lst = [90, 50, 60, 87, 123, 110]
lst_new = sorted(lst)
print(lst_new)
