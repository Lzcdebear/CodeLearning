#判断是否是素数
define issushu(n):  
    if n<=1:
        return 0
    for i in range(2, n):
        if n%i = 0:
            return 0
    else:
        return 1

n=int(input('n='))

issushu(n)  
if w ==1:
    print(n,"是素数！")
else:
    print(n,"不是素数！")
