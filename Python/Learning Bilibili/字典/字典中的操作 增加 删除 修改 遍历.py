# 这里先展示基本的语句
# 先是对于 key 是否在字典中的判断使用 in 或者 not in 语句
scores = {'陆知辰': 20, 'Nikolai': 30, 'Sam': 'dead'}
print('baby' in scores)
# del 函数会删除字典中对应的 key-value 对'
del scores['Sam']
print(scores)
# 而 clear 则会清空字典，使其变为一个空字典
scores.clear()
print(scores)
# 如果想新增 key-value 对，则使用
# 字典名称['key'] = value
scores['Nikolai'] = '陆知辰的老公'
print(scores)
# 修改 key 对应的 value 也十分简单
scores['Nikolai'] = '陆知辰的最爱'
print(scores)
