def MoreThanAvg(L):
    sum,count=0,1
    
    for x in L
        sum+=x[1] 
        count+=1 
    avg=round(sum/count,2)
    print("Avg=",avg)

    for x in L:
        if x[2]>avg:
            print(x[0],x[1])

     #姓名,基本工资,奖金
Ls=[['Holland',6000,2000],['Robbie',5500,3100],['Watson',11000,5200],['Ronan',9000,2600],['Lawrence',5000,2000],['Alex',12000,8000]]


MoreThanAvg(Ls)

