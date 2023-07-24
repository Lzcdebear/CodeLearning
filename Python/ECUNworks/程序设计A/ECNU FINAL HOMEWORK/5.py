"""
5按照下列要求。
程序功能：从键盘输入一行单词（单词之间以空格相隔），要求计算并显示单词个数、总长度、最长单词的长度和对应的单词。
程序运行结果如下图所示：

请输入一行单词：student  classroom  python  good  table
单词共有5个，总长度为31。
其中最长的单词长度是9,对应的单词是：classroom
请输入一行单词：wonderful  road  VIP  classroom  teaching  beautiful
单词共有6个，总长度为42。
其中最长的单词长度是9,对应的单词是：wonderful,classroom,beautiful
"""

def length(x):
    l = 0
    for i in x:
        l += 1
    return l

w_length = []
w_in = input('请输入一行单词：')
w_list = w_in.split('  ')
w_total = 0
w_num = length(w_list)
for i in w_list:
    w_length.append(length(i))
for i in w_length:
    w_total += int(i)
max_length = 0
max_num = []
max_all = []
max_all_length = 0
k = 1
for i in w_length:
    if i > max_length:
        max_length = i
for i in range(0, w_num):
    if w_length[i] == max_length:
        max_num.append(i)
for i in max_num:
    max_all.append(w_list[i])
    max_all_length += 1
print('单词共有', w_num, '，总长度为', w_total, sep='')
print('其中最正常的单词长度是', max_length, ',对应的单词是：', sep='', end='')
for i in max_all:
    print(i, end='')
    if k < max_all_length:
        print(',', end='')
    k += 1
