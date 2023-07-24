# index的作用就是查找指定列表中的指定的元素的索引到底为多少
# 但是当遇到相同的对象的时候，index只会输出第一个对象的索引然后就会结束
av = ['Nik', 'Lzc', 8898, 'Love']
print(av.index('Nik'))
# 这里注意查找索引的格式是 列表 . index (查找的对象)，格式一定要注意正确
# 索引还可以以一下的形式进行查找 对象 开始 结束，在指定的区间内查找是否有想要查找的函数
print(av.index('Nik', 2, 4))
print(av.index('Nik', 1, 4))
print(av.index('Nik', 0, 2))
