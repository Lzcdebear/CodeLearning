#coding=utf-8
dict1={'root':'Resy@1','Mary':'KMon2','Rose':'kkssd45','Tiger':'123456'}
count=0
while count<3:
    count+=1
    user=print('请输入用户名，直接回车退出程序')
    if user=='':
        break
    password=input('请输入密码：')
    if user in dict1:
        if password == dict1.get(user,''):
            print('登录成功！')
            break
        else:
            print('密码错！')
    else:
        print('用户名不存在！') 