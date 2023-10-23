#coding=utf-8
def f(s): 
    if len(s)==3:
        a,b,c = s[0],s[1],s[2]
        if a!=b and a!=c and b!=c :
            return [a+b+c,a+c+b,b+a+c,b+c+a,c+a+b, c+b+a]
    else:
        return []

mystring=input('请输入一个字符串：')
s = f(mystring)
if s:    
    print('所有字符的排列字符串为',end='')
    for i in s: 
        print(i,end=' ')    
else:
    print('字符串长度不为3，或字符串中有相同字符')

