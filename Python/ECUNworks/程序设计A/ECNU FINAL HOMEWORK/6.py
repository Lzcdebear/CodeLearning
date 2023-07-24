"""
计算因子
程序功能：从键盘输入一组整数（整数间以西文半角逗号相隔，回车结束），计算每个整数的真因子（即除了自身以外的约数），以及真因子数不少于4个的整数的个数。
要求：
1：定义一个函数，函数参数为一个整数，返回值为该整数的所有因子构成的列表（该数本身除外的因子）
2：循环遍历输入的这组整数，调用1中定义的函数，并输出如下图所示的结果。

请输入一组整数：6,12,77,30,98
6的真因子有：	1,2,3
12的真因子有：	1,2,3,4,6
77的真因子有：	1,7,11
30的真因子有：	1,2,3,5,6,10,15
98的真因子有：	1,2,7,14,49
真因子数不少于4个的整数共有3个。
"""
# 不要在意任何 warning，本程序就靠 warning 进行运转
def num(x):
    a = [1]
    for i in range(2, x):
        if x % i == 0:
            a.append(i)
    return a

# 这里是第一部分： 打印真因子
ori_str = input('请输入一组整数：')
ori_lst = ori_str.split(',')
ori_len = len(ori_lst)
num_length = []  # 这里存放的是各个数字的约数
for i in ori_lst:
    i = int(i)
    num_length.append(num(i))

# 这里是第二部分： 打印约数大于等于 4 的数字个数
right = 0
len_num = []
for i in num_length:
    len_num.append(len(i))
for i in len_num:
    if i >= 4:
        right += 1
# 这里是第二部分结束

for i in range(0, ori_len):
    j = 0
    while j < len(num_length[i]):
        num_length[i][j] = str(num_length[i][j])
        j += 1
    yinzi = ','.join(num_length[i])
    print(ori_lst[i], '的真因子有：\t', yinzi, sep='')
print('真因子数不少于4个的整数共有', right, '个。', sep='')
# print(ori_lst, ori_len, ori_str, num_length, sep='\n')
# ['6', '12', '77', '30', '98']
# 5
# 6,12,77,30,98
# [[1, 2, 3], [1, 2, 3, 4, 6], [1, 7, 11], [1, 2, 3, 5, 6, 10, 15], [1, 2, 7, 14, 49]]
