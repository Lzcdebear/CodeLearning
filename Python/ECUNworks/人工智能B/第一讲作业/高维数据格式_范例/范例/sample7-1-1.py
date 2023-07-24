#filename: sample7-1-1.py
f = open("c:\\sample\\test1.csv","w")
head = "name,age,sex,phone"
line1 = "张三,29,男,11111111"
line2 = "李四,21,男,22222222"
print(head,file=f)  #将head内容写入参数file指定的文件
print(line1,file=f)
print(line2,file=f)
f.close()
