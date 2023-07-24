#输入n数，n个数之间用逗号间隔，统计这n个数据的方差和标准差。
#L1 = [x1,x2, ..., xn]
#x_bar = sum(L1)/n
#var = (x1**2 + ... + xn **2)/n - x_bar**2


import math
def var(L1):
    s,psum=0,0
    for i in range(len(L1)):
        v=L1[i]
        s+=v
        psum+=v*v
    s=s/len(L1)
    mse=psum/len(L1)-s*s
    return mse

#txt = 5,3,7,8,14,9,12,6
#L1=[5,3,7,8,14,9,12,6]
#L1 = [int(i) for i in input().split(',')]
txt = input()
L1 = txt.split(',')
L1 = [int(i) for i in L1]

dx=var(L1)
print(f'方差为：{dx:.2f}')
mse=math.sqrt(dx)
print(f'标准差为：{mse:.2f}')
