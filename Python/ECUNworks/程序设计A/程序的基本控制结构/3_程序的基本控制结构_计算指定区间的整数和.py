m = int(input(''))
n = int(input(''))
if m <= n:
    x = m
    y = n
else:
    x = n
    y = m
# x是比较小的那个，y是比较大的那个
i = x
a = 0
while i <= y:
    a = a + i
    i += 1
print(x, '+...+', y, '=', a, sep='')
