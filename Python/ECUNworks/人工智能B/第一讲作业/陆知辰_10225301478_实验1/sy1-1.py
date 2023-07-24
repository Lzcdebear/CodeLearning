import csv
f = open("F:\\Python\\第一讲作业\\陆知辰_10225301478_实验1\\city_temp.csv", "w", newline='')
# 处理city数据
city1 = {1: -18, 2: -15, 3: 0, 4: 10, 5: 24, 6: 28, 7: 30, 8: 30, 9: 25, 10: 12, 11: 5, 12: -10}
city2 = {1: 5, 2: 16, 3: 20, 4: 25, 5: 30, 6: 35, 7: 38, 8: 38, 9: 35, 10: 30, 11: 20, 12: 15}
title = ['城市', '月份1', '月份2', '月份3', '月份4', '月份5', '月份6', '月份7', '月份8', '月份9', '月份10', '月份11',
         '月份12']
city1t = ['北方甲市']  # city 1 temperature
city2t = ['南方乙市']  # city 2 temperature
for i in city1.keys():
    city1t.append(city1[i])
for i in city2.keys():
    city2t.append(city2[i])
# 写入文件
writer = csv.writer(f)
writer.writerow(title)
writer.writerow(city1t)
writer.writerow(city2t)
f.close()
