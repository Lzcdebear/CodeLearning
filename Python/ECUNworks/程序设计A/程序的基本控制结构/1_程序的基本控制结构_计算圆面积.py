import math
r = float(input(''))
if r < 0:
    print('r=', 'ERROR', sep='')
else:
    s = math.pi * pow(r, 2)
    print('r=', format(s, '.3f'), sep='')
