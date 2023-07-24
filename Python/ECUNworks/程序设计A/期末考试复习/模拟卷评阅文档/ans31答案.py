def getCelsius(f):   #此句无错误
        c= (f- 32) *5/9
        return c

f=float(input('输入华氏温度:'))       #输入华氏温度
c= getCelsius(f)   #求摄氏温度
print("hsd=%.1f, ssd=%.1f"%(f,c)); #输出结果
