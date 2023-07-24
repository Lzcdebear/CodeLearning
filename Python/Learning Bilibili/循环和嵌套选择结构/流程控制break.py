# 用于停止结束跳出循环结构，属于非正常结束循环
# 例子：能够输入密码三次，如果正确结束，如果不正确则重新输入，错误三次结束循环要求等待15min
for item in range(3):
    pw = input('Enter your passwords')
    if pw == 'Nik is the best husband in the world':
        print('welcome back, my boy')
        break
    else:
        print('Sorry, wrong password')
    if item == 3:
        print('Please try again after 15 min')
