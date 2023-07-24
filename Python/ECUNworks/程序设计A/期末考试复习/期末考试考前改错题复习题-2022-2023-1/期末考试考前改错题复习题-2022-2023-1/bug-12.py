def gt5(s)
    gt5s=0
    for c in s:
        if c>='5' and c<='9':
            gt5s+=1
    return

while True:
    s=input("请输入带数字的字符串，end结束程序：")
    if s.lower()=='end':
        continue
    print('字符串为"%s"，其中单个数字大于等于5的有%d个'%(s,gt5(s)))
