average = lambda x, y, z: (x + y + z) / 3
a = int(input())
b = int(input())
c = int(input())
ave = "%.2f" % average(a, b, c)
print('average=', ave, sep='')
