chinese = [76, 63, 79, 82, 53, 78, 67]
math = [88, 56, 78, 92, 69, 75, 82]
n = int(len(chinese))
total = []
i = 0
s = 0
while i < n:
    chi = int(chinese[i])
    mat = int(math[i])
    tol = chi + mat
    total.append(tol)
    i += 1
print('每位成员总分：', total, sep='')
maxi = int(total[0])
for j in total:
    s = s + j
    if int(j) > maxi:
        maxi = int(j)
ave = round(s / n, 2)
print('最高总分：', maxi, ',', '小组平均分：', ave, sep='')
