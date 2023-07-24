# range用于生成一个整数的数列
# 第一种创建方式range(stop)，生成一个从0到stop的一个数列步长为1,到stop结束但是不包括stop这个数
r = range(10)
print(r)
# 直接print只会展示stop的迭代式子，要想展示range中的所有对象要使用list
print(list(r))
# 可以看到r中有10个数字，虽然range到10，但是r最大为9
# 第二种创建方式就是range(start, stop)
r = range(1, 10)
print(list(r))
# 这里的range都是一样的，到10结束但是不包括10
# 第三种方式就是range(start, stop, step)同样包括start，不包括stop
r = range(1, 11, 2)
print(list(r))
# 可以看到没有11
# 进行查找的时候可以使用in或者not in来将对象查看是否在range中
print(10 in r)
print(10 not in r)
# range的优势在于这个式子中无论数字多大或者多长，占用的内存空间都是一样的，只会存储三个 start stop step
# 利用这个性质可以将range用在一些结构中作为一些整数对象的代替，因为占用的内存较小，所以实际中更加方便快捷，也更加简单明了
