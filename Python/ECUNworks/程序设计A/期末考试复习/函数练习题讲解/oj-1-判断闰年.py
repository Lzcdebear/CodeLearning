#年份由键盘输入。
#（1）编写isLeap(year)函数,判断year是否为闰年，如果是返回True否则False。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬
#（2）在主程序中调用isLeap函数，如果是闰年则输出“XXXX年是闰年”，否则，输出“XXXX年不是闰年”。
def isLeap(year):
    return (year%4==0 and year%100!=0) or (year%400==0)
    
year = int(input())
flg = isLeap(year)
#if isLeap(year):
if flg:
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")
            