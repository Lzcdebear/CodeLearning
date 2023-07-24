# 字典中元素可以使用 [] 或者 get 函数两种方式
# [] 和列表是相似的
scores = {'陆知辰': 20, 'Nikolai': 30}
print(scores['Nikolai'])
# 但是如果 [] 中的 key 不存在字典里，则会报错 keyError
# 使用 get 函数输入一个不存在于字典中的 key ，则会输出 None
print(scores.get('Nikolai'))
print(scores.get('Lover'))
# get 还可以设置默认值
print(scores.get('LOVER', 99))
print(scores.get('Nikolai', 100))
# 这个默认值就是如果当前的 key 没有在字典中出现，那么就会输出默认值
# 但是如果 key 在字典中出现，则会输出字典中对应 key 的 value
