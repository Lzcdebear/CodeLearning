# else除了能够和if条件语句一起使用以外，还可以和for或者while一起使用
# 这里的原则就是如果没有遇到break，那么就执行else
for i in range(3):
    pw = input('Enter your password')
    if pw == 'nik is my husband':
        print('welcome back, master')
        break
    else:
        print('Sorry, the password is wrong.')
        print('Please try again')
else:
    print('three times error, please try again after 5 min')
# 接下来再用while展示同样的效果
a = 0
while a < 3:
    pw = input('Enter your password')
    if pw == 'nik is my husband':
        print('welcome back master')
        break
    else:
        print('Sorry the password is wrong')
        print('Please try again')
    a += 1
else:
    print('Three times error, please try again after 5 min')