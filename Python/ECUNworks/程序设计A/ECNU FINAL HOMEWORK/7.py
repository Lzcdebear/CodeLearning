"""
给成绩打标记
程序功能：根据用户输入的多个学生姓名和成绩，按姓名升序输出每个人的姓名和成绩等级。
输入格式：输入时以空格隔开的多人记录，逗号隔开的每人姓名和成绩，（比如：豆豆,85 小胖,92 八戒,19），成绩均为正整数。
等级划分规则：70分以下为D，70～79为C， 80～89为B，90～100为A。
输出结果中姓名和等级（包括表头和数据）两列之间用制表符分隔，不能用空格调整；按姓名排序，得到运行示例的顺序。
程序运行示例如下所示：
要求
1：设计函数mark，参数为成绩，返回值为等级划分
2：调用函数得到每位同学的等级
3：按姓名排序并输出

在下方输入空格隔开的多人成绩记录（半角逗号隔开的每人姓名和成绩）：
金不换,59 舒德清,79 计德柱,60 刀快,84 袁组,93
姓名	等级
刀快	B
舒德清	C
袁组	A
计德柱	D
金不换	D

"""
# Part 1  定义函数 mark
def mark(x):
    x = int(x)
    if x >= 70:
        if x >=80:
            if x >=90:
                mrk = 'A'
            else:
                mrk = 'B'
        else:
            mrk = 'C'
    else:
        mrk = 'D'
    return mrk

# Part 2  定义函数 name_rank 用于帮助获取 姓名 来进行排序
def name_rank(t):
    return t[0]

# Part 3  定义一个二维列表
a = input('在下方输入空格隔开的多人成绩记录（半角逗号隔开的每人姓名和成绩）：').split(' ')
for i in range(0, len(a)):
    a[i] = a[i].split(',')
    a[i][1] = mark(a[i][1])
print(a)
rank = sorted(a, key=name_rank)
print(rank)

# Part 4  进行打印
print('姓名\t等级')
for i in range(0, len(rank)):
    rank[i] = '\t'.join(rank[i])
    print(rank[i])
    