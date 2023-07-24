a = float(input(''))
b = a
y = 0
while b < a * 2:
    b = b * (1 + 0.0225)
    y = y + 1
print(y, '年后存款会翻翻', sep='')
