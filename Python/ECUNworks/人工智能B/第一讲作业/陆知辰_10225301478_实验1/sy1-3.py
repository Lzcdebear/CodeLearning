import csv
f = open("F:\\Python\\第一讲作业\\陆知辰_10225301478_实验1\\city_temp.csv")
lines = csv.reader(f)
line = list(lines)
city1 = line[1]
city2 = line[2]
legth = len(city1)
delttemp = []
maxt = -100000
maxn = 0
# 求温度差
for i in range(1, legth):
    a1 = float(city1[i])
    a2 = float(city2[i])
    delttemp.append(abs(a1 - a2))
# 求最大值
for i in range(0, len(delttemp)):
    if maxt >= int(delttemp[i]):
        continue
    else:
        maxt = int(delttemp[i])
        maxn = i + 1
print('温差最大的月份是{}月份，温差是{}摄氏度'.format(maxn, maxt))
