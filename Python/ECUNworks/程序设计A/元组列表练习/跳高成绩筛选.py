group = ((78, 150, 90, 102, 110, 141),
         (149, 88, 132, 95, 108, 112, 143),
         (100, 123, 125, 99, 106, 118, 133),
         (152, 86, 132, 95, 70, 122, 149, 124))
a = []
print('获得初赛资格的成绩')
for i in range(4):
    n = len(group[i])
    for j in range(n):
        if group[i][j] >= 142:
            a.append(group[i][j])
        else:
            continue
    print('第', i + 1, '组:', sep='', end='\t')
    print(*a, sep=' ', end='\n')
    a = []
