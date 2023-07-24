# print说明
# print可以用于数字输出
print(1)
# print可以用于字符串输出
print('hello world')
# print可以用于运算符输出
print(1+2+3)
# print可以输出文件，位置 D/LZC/Python notes/print test.txt
fp = open('D:/LZC/Python notes/print test.txt', 'a+')
print('hello world', file=fp)
fp.close()
# 以上为自动换行的输出
print('hello', 'world', 'Python')
# 以上为输出不同内容但是不换行的方法

name = 'fuck'
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)
