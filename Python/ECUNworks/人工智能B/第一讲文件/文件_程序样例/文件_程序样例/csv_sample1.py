with open("ranks.csv") as f:    #打开文件供读
        for line in f:          #迭代读取每一行
                L = line.strip().split(',') #行去掉首尾空白字符后分隔
                for i in range(len(L)):
                        print(L[i],end="\t")	                
print()
