def sumOfDig(s):
    sumdig=0
    for c in s:
        if c>=0 and c<=9:
            sumdig+=c
    return sumdig

while True:
    s=input("请输入带数字的字符串，quit结束程序：")
    if s.lower()='quit':
        break
    print(f'字符串为{s}，其中单个数字累加和为{sumOfDig(s)}') 