# 题目 1
# 输入身份证号码，输出这人的出生年月和性别
# 倒数第二位是性别，单数是男，双数是女
"""
idc = input('请输入身份证号')
yer = idc[6:10]
mon = idc[10:12]
sex = int(idc[16:17])
if sex % 2 == 0:
    print('生日年月是', yer, mon)
    print('是个女人')
else:
    print('生日年月是', yer, mon)
    print('是个男人')
"""
# 题目 2
# 给出一个整数,返回代表该值的英文，限定输入的数在0到99
"""a = input('请输入一个整数')
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ans = []
for i in a:
    b = int(i)
    p = eng[b]
    ans.append(p)
enged = '-'.join(ans)
print('你输入的数字是', a, '的英文是', enged, sep='')
"""
# 题目 3
# 使用random 模块中的randint()生成一个随机数集合：从0 到9(包括9)中的随机数。这些数字组成集合A。
# 同理，按此方法生成集合B。显示结果 A | B 和 A & B
"""import random
i = 0
a = set({})
a.add(str(random.randint(0, 9)))
b = set({})
b.add(str(random.randint(0, 9)))
c = a & b
d = a | b
if len(c) == 0:
    print('A & B 为空集')
else:
    print('A & B = ', ''.join(c))
print('A | B = ', ' '.join(d))
"""
# 题目 4
# 创建一个简单的学生成绩管理系统，用户每次输入下面的一行输入，把该行数据保存到列表中，
# 然后把列表中的第一列学号作为键，列表作为值创建字典。
# 1001,张三,100
# 1002,李四,90
# 1005,王五,80
# 1003,刘六,96
# 1004,高七,85
# 1006,朱十,83
"""
dic = {}
i = 0
lst = []
for i in range(6):
    a = input('number,name,performance')
    b = a.split(',')
    dic[b[0]] = ' '.join(b[1:])
m = sorted(dic.keys())
for i in range(6):
    p = str(m[i])
    q = str(dic[p])
    print(p + q)
"""
