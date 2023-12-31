# 循环结构的第二种方式for in。其中的in的意思就是遍历，就是将其中的所有对象都拿出来一一对照
# 其中能遍历的对象只有字符串和序列等，也就是可迭代对象这一类
# for 自定义的变量 in 可迭代对象  意思就是将可迭代对象中的每一个对象都按照顺序赋给自定义的变量
# 当in后面的对象选择的是字符串的时候，就会将字符串里的每一个字符依次付给自定义的变量，这里的变量可以直接在for后面定义
for item in 'I like physics':
    print(item)
# 注意两点，语法中的：不要忘记，打印出来的字符是每个字符都会进行换行，类似竖向文本框
# 当in后面的对象选择的是序列的时候，就会将序列中的每一个对象按照顺序进行迭代
for item in range(10):
    print(item)
# 这里虽然只有打印到9，但是有10个数字，也就是意味着运行了10次
# 这里的自定义变量也不一定需要定义，如果只是用来作为循环的一个过程，后续步骤中不需要使用这个变量的话，可以使用下划线进行代替
for _ in range(5):
    print('I Love Nicholai')
'''
例题：寻找100-999之间的水仙花数
举例
153 = 3*3*3 + 5*5*5 + 1*1*1
'''
a = 0
for item in range(100, 999):
    ge = item % 10  # 取到个位的数字
    shi = item // 10 % 10  # 取到十位的数字
    bai = item // 100  # 取到百位的数字
    if item == ge ** 3 + shi ** 3 + bai ** 3:
        print(item)
        a += 1
print('这里一共有 ', a, ' 个水仙花数')
