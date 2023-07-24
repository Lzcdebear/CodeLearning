# 这里将会列举不可以作为python文件或者字符串名字的word
import keyword
print(keyword.kwlist)
# 所以在运行+运算的时候只是将两个字符串相连，需要转化数据类型来进行运算
a = input('请输入第一个数字')
b = input('请输入第二个数字')
print(float(a) + float(b))
print(type(a), type(b))
# 这里提供一种较为简单的input的方式，如果是数字的话可以直接将转化放在赋值一起
c = float(input('The first number'))
d = float(input('The second number'))
print(c + d)
print(type(c), type(d))
# 以上两种方法的区别就是
# ab依旧是字符串类型，后续使用需要再次转换
# cd将不是字符串类型，后续使用直接为浮点型或者整型
