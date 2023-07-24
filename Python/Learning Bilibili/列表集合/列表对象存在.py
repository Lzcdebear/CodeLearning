# 对于列表中是否存在一个对象可以使用in或者not in来进行查找
lst = [10, 20, 'python', 'me']
print(10 in lst)
print('g' not in lst)
# 想要依次获得列表中的对象，可以使用for
for item in lst:
    print(item)
