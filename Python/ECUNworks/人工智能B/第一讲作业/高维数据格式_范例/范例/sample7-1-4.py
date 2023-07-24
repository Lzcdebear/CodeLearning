#filename: sample7-1-4.py
import csv
csvfile = open("c:\\sample\\test2.csv")
lines = csv.reader(csvfile)	   #生成reader对象
for line in lines:             #从reader对象中遍历各行
    print(line)              #line对应row对象，是包含行中各字段的列表
csvfile.close()
