#辗转相除求最大公约数
def hcf(u,v):
    if v>u:
        u,v=v,u  # 两个数的交换，保证u>v
    r = u%v   #看u能被v整除
    while r!=0: #u不能被v整除，假如r==0，说明u能被v整除，结束循环
        u=v
        v=r
        r=u%v
    return v

def lcd(u,v,h):
    return u*v/h

u=int(input(""))
v=int(input(""))
h=hcf(u,v)
print(f"{u}和{v}的最大公约数为{h}")
l=lcd(u,v,h)
print(f"{u}和{v}的最小公倍数为{l}")
