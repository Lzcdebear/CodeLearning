from cmath import pi

x1 = 0.0
while x1 != 100:
    a = 4 * pi * (10 ** -7) * 500 * 0.01 * 0.1
    x2 = (x1/100) * (x1/100)
    b = 2 * ((0.01 + x2) ** (1.5))
    fin = a / b
    print(fin)
    x1 = float(input('请输入距离'))

