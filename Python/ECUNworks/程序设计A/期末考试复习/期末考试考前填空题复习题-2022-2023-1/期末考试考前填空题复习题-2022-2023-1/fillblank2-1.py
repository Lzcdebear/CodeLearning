lst = [1,2,3,4,5]

dic = _____
for n in lst:
    dic[n] = 0

while True:
    n = ____(input("请输入你的选票1-5,输入-1则退出：\n"))
    if n == -1 :
        _______
    if 1 <= n <= 5 :
        dic[n] = dic[n] + _____

for n in lst:
    print ("%d号人的票%d" % (n,_____))
