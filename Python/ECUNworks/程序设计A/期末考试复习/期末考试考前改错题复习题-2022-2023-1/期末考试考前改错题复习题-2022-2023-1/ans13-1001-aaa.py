def filterLst(L):
    outL=[]
    for x in L:
        for i in range(x+1):
            if i*i==x:
                outL.append(x)
    #print('L--->',L)
    #print('outL--->',outL)
    return outL
s=input("请输入一组整数:（以西文半角逗号方式间隔）")
data=s.split(',')
for i in range(len(data)):
    data[i]=int(data[i])
result=filterLst(data)
if len(result)!=0:
    print ("完全平方数有",result)
else:
    print ("无符合要求的数！")
