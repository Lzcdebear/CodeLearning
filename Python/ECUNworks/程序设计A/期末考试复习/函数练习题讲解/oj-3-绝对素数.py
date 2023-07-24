#1 num是素数
#2 num反过来也是素数
#3 num 不是对称数
#4 前40个绝对素数 
from math import sqrt

#判断一个数是不是素数
def isPrime(n):
    if n<2:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True
#取的数的逆序数    
def ReverseNum(n):
        return int(str(n)[::-1])

#判断是不是绝对素数        
def isReversePrime(n):
        #return isPrime(n) and isPrime(ReverseNum(n)) and n!=ReverseNum(n)
        reversenum = ReverseNum(n)
        if n == reversenum:
            return False
        flg1  = isPrime(n)
        if flg1 == False:
            return False
        flg2 = isPrime(reversenum)
        if flg2 == False:
            return False
        return True
        
        
def main():
    lst = []
    j=2
    while True:
        if isReversePrime(j):
            lst.append(j)
        if len(lst) == 40:
            break
        j+=1
    for i in range(len(lst)):
        x = lst[i]
        print(x,end='\t')
        if (i+1) % 10 == 0:
            print(end='\n')
        
main()