iimport csv
with  open("phonelist.csv","w",newline='') as csvfile:	#打开文件写
        writer = csv.writer(csvfile)	#构造writer对象
        writer.writerow(("name","age","sex","phone"))	#写入标题行
        writer.writerow(("张三","29","男","11111111"))	#写入数据行
        writer.writerow(("李四","21","男","22222222"))

