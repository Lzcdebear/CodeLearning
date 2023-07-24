# continue用于结束当前的循环或者分支，进入下一个循环
# 和break不同的是，break直接推出循环，意味着循环内一切将不会在被运行
# 而continue则是当前的循环结束，从头重新进行循环，就是进入下一个新的循环
# 例子
# 打印1-100所有能被5整除的数字
for item in range(1, 101):
    if item % 5 != 0:
        continue
    else:
        print(item)
