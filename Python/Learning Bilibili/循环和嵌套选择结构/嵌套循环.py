# 这里展示嵌套循环，也就是在一个循环内加入另一个循环
# 这里先展示打印三行四列的矩阵
for i in range(1,4):
    for j in range(1,5):
        print('*', end='\t')  # 这里表示的是不换行输出,\t就是空格的意思
    print()  # 这里表示的是换行
# 这里展示打印九行的三角形
for i in range(1,10):
    for j in range(1,i+1):  # 这里表示的意思是打印的个数和行数是一样的
        print('*', end='\t')
    print()
# 这里再来展示一下九九乘法表的输出方式
for i in range(1,10):
    for j in range(1,i+1):  # 这里表示的意思是打印的个数和行数是一样的
        print(i, '*', j, '=', j * i, end='\t')
    print()
# 可以看到这样就可以打印九九乘法表了
