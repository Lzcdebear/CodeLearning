# 这里展示pass的使用方法，pass的作用就是利用pass构建一个空语句，pass没有任何意义，但可以使程序运行，将构思好的程序运行
# 这里使用条件语句进行展示
money = 1000
a = int(input('请输入取款金额'))
if money >= a:
    print('余额为：  ', money - a)
else:
    print('余额不足')
# 这里的语句都是完整的，但是设计过程中倘若没有想好if后和else后的内容，就可以pass，使程序不报错，语法正确
money = 1000
a = int(input('请输入取款金额'))
if money >= a:
    pass
else:
    pass
