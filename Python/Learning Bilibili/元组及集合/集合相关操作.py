# 集合元素的判断
s = {10, 20, 30, 40, 60}
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)
# 集合元素的增加
'''
有两种方式可以进行增加
第一种使用 add 一次只能增加一个元素
第二种使用 update 一次至少增加一个元素
并且在使用 update 的时候不一定只能增加集合，还可以是列表，元组
'''
s.add(80)
print(s)
s.update({125, 261, 489})
print(s)
s.update([164, 187])
s.update((789, 456))
print(s)
# 集合中元素的删除
'''
第一种使用 remove 一次删除一个元素，如果元素不存在则报错 key error
第二种使用 discard 一次删除一个元素，如果元素不存在不报错
第三种使用 pop 一次删除随机一个元素,不能添加参数
第四种使用 clear 一次删除所有元素
'''
s.remove(456)
print(s)
s.discard(789789789789)
print(s)
s.pop()
print(s)
s.pop()
print(s)
