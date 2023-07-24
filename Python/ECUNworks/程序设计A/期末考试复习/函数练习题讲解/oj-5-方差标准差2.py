import math
def var(L1):
    s = sum(L1)/len(L1)
    lst = [(x -s)**2 for x in L1]
    mse=sum(lst)/len(lst)
    return mse
# txt = 5,3,7,8,14,9,12,6
#L1=[5,3,7,8,14,9,12,6]

txt = input()
L1 = txt.split(',')
mp = map(int,L1)
L1 = list(mp)

dx=var(L1)
print(f'方差为：{dx:.2f}')
mse=math.sqrt(dx)
print(f'标准差为：{mse:.2f}')
