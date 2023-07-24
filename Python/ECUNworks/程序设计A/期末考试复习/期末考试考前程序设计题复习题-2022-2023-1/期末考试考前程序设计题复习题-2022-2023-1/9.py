#ans41_lzc.py

t=float(input("请输入温度："))
if t!=999:
    maxt=t
    mint=t
    s=0
    n=0
    while True:
        t=float(input("请输入温度："))
        if t == 999:
            break
        if t>maxt :
            maxt=t
        elif t<mint:
            mint=t
        s+=t
        n=n+1
    print(f"最高温度：{maxt},最低温度：{mint},平均温度：{s/n:.2f}")
        
        
    
