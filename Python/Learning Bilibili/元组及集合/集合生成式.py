# 其实集合的生成式和列表的生成式是一样的，只要将 【】 改变为 {}
print('以下是列表生成式')
print(
    '''
    # 这东西也就是列表生成的公式
    # 可以使用 for 语句来进行生成整数数列
    lst = [i for i in range(1, 10)]
    print(lst)
    解释一下这个公式
    第一个 i 是表达式子，类似于数列的通项公式
    后面的 for 语句就是将 i 一个个取遍
    lst = [i*i for i in range(1, 11)]
    print(lst)
    '''
)
