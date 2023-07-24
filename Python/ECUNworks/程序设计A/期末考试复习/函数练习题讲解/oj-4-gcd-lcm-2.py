#辗转相除求最大公约数
def hcf(u,v):
    set_u = []
    for i in range(1,u+1):
        if u % i == 0:
            set_u.add(i)
    set_v = []
    for i in range(1,v+1):
        if v % i == 0:
            set_v.add(i)
    
    set_uv = set_u & set_v
    return max(set_uv)
    
def lcd(u,v,h):
    return u*v/h

u=int(input(""))
v=int(input(""))
h=hcf(u,v)
print(f"{u}和{v}的最大公约数为{h}")
l=lcd(u,v,h)
print(f"{u}和{v}的最小公倍数为{l}")
