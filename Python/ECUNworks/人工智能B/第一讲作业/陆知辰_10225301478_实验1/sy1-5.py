import csv
import json

f = open("F:\\Python\\第一讲作业\\陆知辰_10225301478_实验1\\city_temp.csv")
lines = csv.reader(f)
line = list(lines)
city1 = line[1]
city2 = line[2]


# 函数作用将原来地列表转化为月份对应温度的字典
def turndic(x):
    numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    valuelist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    mon = {numlist: valuelist for numlist, valuelist in zip(numlist, valuelist)}
    tem = x[1:]
    a = 0
    for j in mon:
        mon[j] = tem[a]
        a += 1
    return mon


mon1 = turndic(city1)
mon2 = turndic(city2)
mon1fin = json.dumps(mon1, ensure_ascii=False)
mon2fin = json.dumps(mon2, ensure_ascii=False)
print(city1[0], mon1fin, sep='：')
print(city2[0], mon2fin, sep='：')
