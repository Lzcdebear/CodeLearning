import datetime

"""
说实话我真的不知道这个作业是什么意思，如果说这个作业默认现在的时间是2020-9-1
那么无论什么时候我去做这个作业应该结果都是一样的
但是我之前做和现在做的结果是不一样的，好像答案是按照现在现实的时间进行计算的
所以反正我都写了，就全部放上去了，下面注释中的就是原来做的，之前能通过但是后面就通不过了的
注释以外的是新按照现实时间写的
"""
'''
import time
time_tuple = time.localtime(time.time())
print(time.localtime())
print("今天是{}-{}-{}".format(time_tuple[0], time_tuple[1], time_tuple[2]))
tom = int(time_tuple[1])
tod = int(time_tuple[2])
idc = input('请输入身份证号码：')  # 身份证号码
mm = idc[10:12:1]
dd = idc[12:14:1]
m = int(mm)
d = int(dd)
x = 0
if m < tom:
    print('今年生日已过！')
if m == tom and d < tod:
    print('今年生日已过！')
if m == tom and d < tod:
    x = d - tod
    print('今年生日还有', x, '天', end='')
if m > tom:
    x = d - tod
'''
time_now = datetime.datetime.now()
print('今天是' + datetime.datetime.now().strftime("%Y-%m-%d"))
yy = str(time_now.year)
idc = input('请输入身份证号码：')  # 身份证号码
mm = idc[10:12:1]
dd = idc[12:14:1]
birthday = yy + '-' + mm + '-' + dd
birth = datetime.datetime.strptime(birthday, '%Y-%m-%d')
final_time = birth - time_now
x = final_time.days
delta_time = int(x)
if delta_time < 0:
    print('今年生日已过！')
else:
    print('今年生日还有', delta_time, '天', end='')
