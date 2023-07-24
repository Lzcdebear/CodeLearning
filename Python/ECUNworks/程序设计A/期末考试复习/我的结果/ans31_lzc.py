def getCelsius(f):  # 此句无错误
    c = (f - 32) * 5 / 9
    return c


h = input('输入华氏温度:')  # 输入华氏温度
s = getCelsius(float(h))  # 求摄氏温度
print("hsd=%.1f, ssd=%.1f" % (float(h), float(s)))  # 输出结果
