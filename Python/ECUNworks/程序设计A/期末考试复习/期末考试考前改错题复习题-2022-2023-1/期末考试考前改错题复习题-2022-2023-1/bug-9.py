def hcf(u,v):
    if u>v
        m=v
    else:
        m=u
    for i in range(m,1,-1):
        if (u%i==0) and (v%i==0):
            return u

u=int(input("请输入第一个整数："))
v=int(input("请输入第二个整数："))
h=hcf(u,v)
print(f"{u}和{v}的最大公约数为：{h}")

