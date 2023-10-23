#coding=utf-8
while True:
    i=int(input("请输入1-10之间的整数(输入 '0' 退出程序):\n"))
    if i==0:                        
        break
    for j in range(i,0,-1):         
        #打印10-j个空格，不换行
        print(10-j,end='')
        #打印j*2-1个字母，提示：chr(65)为A
        print(chr(j)*(2*j-1))
    print()
