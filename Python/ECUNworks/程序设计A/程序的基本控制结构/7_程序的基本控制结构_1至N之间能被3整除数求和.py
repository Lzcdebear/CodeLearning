a = int(input(''))
x = 0  # 这是存储所有数字之和
for i in range(1, a+1, 1):
    if i % 3 == 0:
        x = x + i
    i += 1
print('1-', a, '之间能被3整除的数的和为:', x, sep='')
