import csv


# 判断是否能够满足植物生长
def tempjug(a):
    d = 0
    dmax = 0
    for i in range(1, len(a)):
        if int(a[i]) >= 20:
            d += 1
            if d > dmax:
                dmax = d
        else:
            d = 0
    if dmax >= 7:
        return 1
    else:
        return 0


# 打印相关语句
def jugab(x):
    if x == 1:
        print('满足植物生长需求')
    else:
        print('不满足植物生长需求')


f = open("F:\\Python\\第一讲作业\\陆知辰_10225301478_实验1\\city_temp.csv")
lines = csv.reader(f)
line = list(lines)
city1 = line[1]
city2 = line[2]
jug1 = tempjug(city1)
jug2 = tempjug(city2)
# 最后打印
print(city1[0], end='')
jugab(jug1)
print(city2[0], end='')
jugab(jug2)
