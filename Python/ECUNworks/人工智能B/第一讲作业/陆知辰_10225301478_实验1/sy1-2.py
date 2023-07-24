import csv
f = open("F:\\Python\\第一讲作业\\陆知辰_10225301478_实验1\\city_temp.csv")
# max and min
lines = csv.reader(f)
line = list(lines)
city1 = line[1]
city2 = line[2]
max1 = -100000
maxn1 = 0
minn1 = 0
max2 = -100000
maxn2 = 0
minn2 = 0
min1 = 10000
min2 = 10000
print(city1, city2, sep='\n')
print(len(city1), len(city2), sep='\n')
for i in range(1, len(city1)):
    if max1 >= int(city1[i]):
        continue
    else:
        maxn1 = i
        max1 = int(city1[i])
    if min1 <= int(city1[i]):
        continue
    else:
        minn1 = i
        min1 = int(city1[i])
for j in range(1, len(city2)):
    if max2 >= int(city2[j]):
        continue
    else:
        maxn2 = j
        max2 = int(city2[j])
    if min2 <= int(city2[j]):
        continue
    else:
        minn2 = j
        min2 = int(city2[j])
# 最高气温 max1 max2 出现月份 maxn1 maxn2
# 最高气温 min1 min2 出现月份 minn1 minn2
print('北方甲城市最高温度为{0}摄氏度，出现月份为{1}月份，最低温度为{2}摄氏度，出现在{3}月份'.format(max1, maxn1, min1, minn1))
print('南方乙城市最高温度为{0}摄氏度，出现月份为{1}月份，最低温度为{2}摄氏度，出现在{3}月份'.format(max2, maxn2, min2, minn2))
f.close()
