# 可以通过函数来获得字典中想获得的东西
# 首先是获得 key
scores = {'陆知辰': 20, 'Nikolai': 30}
keys = scores.keys()
print(keys)
# 默认的格式是  dict_keys
print(type(keys))
print(list(keys))
print(type(keys))
# 其他的通过类似方法获得的 value 和 item 默认都是 dict_value/item 格式
value = scores.values()
items = scores.items()
print(value)
print(items)
print(type(value))
print(type(items))
a = list(value)
b = list(items)
print(a)
print(b)
# 这里看到的 b 中的 () 组成的对象叫做 元组及集合
# 接下来展示字典中的遍历
# 使用 for-in 语句获得的只有字典中的 key，如果想获得 value 可以参考《字典中元素的获取》
scores = {'陆知辰': 20, 'Nikolai': 30}
for item in scores:
    print(item)
    print(scores[item])
    print(scores.get(item))
