#ans23_lzc.py
ad = {'Georgia':9919945,
'Hawaii':1392313,
'Idaho':1595728,
'Illinois':12875255,
'Indiana':6537334,
'Iowa':3074186}
bd= {'Illinois':12875255,
'Indiana':6537334,
'Iowa':3074186,
'Kansas':2885905,
'Kentucky':4380415,
'Louisiana':4601893
}

for a in ad:
    if a not in bd:
         bd[a] = ad[a]
for a in bd:
    print('{}:{}'.format(a, bd[a]))
