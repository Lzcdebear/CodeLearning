"""
字典是python中另一种存储数据的类型
字典存储有两个部分  name 和  value
字典定义使用大括号/花括号  {}
字典是一个可变的序列，但是和列表不同的是，字典是没有顺序的，也就是说是没有 1、2、3、4... 的编号的
"""
# 这边展示定义 字典 的方法
scores = {'陆知辰': 20, 'Nikolai': 30}
# 这里的引号内的内容是字典的 key ，后面的数值是 value，
# 字典的使用方式和现实中查字典是相似的，通过 key 来找到对象然后输出 value
# 注意，这里的 key 一定是 不可变动 的类型，也就是说不能使用 list 作为 key，但是后面的 value 并不一定是数值，还可以是字符串
# 这里使用的函数是 hash(key) = value
# key 就是名称，hash 是将 value 和 key 对应上，通过这样的函数重复，形成字典
# 除了上面的这种创建字符的方式，还可以使用内置的函数 dic 来定义字典
s = dict(apple='中文翻译是苹果', num=220)
print(s)
# 字典中的 key 是不能够重复的，但是 value 是无所谓的
# 字典是一种通过更大的占用空间来提升速度的方式。
