"""
按照下列要求，设计完成一个程序。
程序功能：输入一组气温（直到输入999结束），统计这组气温数据的最高气温、最低气温和平均气温。
程序运行示例如下所示

请输入温度：35
请输入温度：36
请输入温度：36
请输入温度：37
请输入温度：36
请输入温度：37
请输入温度：38
请输入温度：39
请输入温度：37
请输入温度：31
请输入温度：999
最高温度：39.0,最低温度：31.0,平均温度：36.33

请输入温度：999
"""

# 这是一个很奇怪的地方
# 我用计算器计算上面这组数据的平均数，算出来是36.2
# 但是答案示例算出来是36.33
# 我觉得是题目出问题了，平均数就是36.2
# 总共十个数字，相加没有达到四位数，算出来的一定是两位小数，所以题目在放屁

stop = False
tol = []
maxi = 0.0
mini = 0.0
summ = 0.0
while stop == False:
    a = float(input('请输入温度：'))
    if a == 999:
        stop = True
    else:
        tol.append(a)
for i in tol:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i
    summ = summ + i
ave = round(summ / int(len(tol)), 2)
print('最高温度', maxi, '最低温度', mini, '平均温度', ave, sep='')
