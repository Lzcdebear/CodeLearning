import math
a = int(input('Enter the a'))
b = int(input('Enter the b'))
c = int(input('Enter the c'))
x1 = ((-b) + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
x2 = ((-b) - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
print(x1)
print(x2)
