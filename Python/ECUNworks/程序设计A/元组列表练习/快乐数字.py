ori = '100,200'
lst = ori.split(',')
lst1 = []
last = 0
p = 1
b = 0
c = 0
mini = int(lst[0])
maxi = int(lst[1])
for i in range(mini, maxi + 1):
    sec = True
    while sec:
        a = str(i)
        for j in a:
            b += int(j) ** 2
        if b == 1:
            q = str(b)
            for k in q:
                c += int(k) ** 2
            if c == 1:
                lst1.append((i, p))
                sec = False
        p += 1
        if p > 2000:
            sec = False
    p = 1
    b = 0
print(lst1)
