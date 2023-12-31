"""
程序功能：身份证号校验。
中国目前采用的是18位身份证号，其第18位是校验位。如果身份证号码的其中一位填错了（包括最后一个校验位），则校验算法可以检测出来。校验规则如下：
1. 将前面的身份证号码17位数分别乘以不同的系数。从第一位到第十七位的系数分别为：7－9－10－5－8－4－2－1－6－3－7－9－10－5－8－4－2。
2. 将这17位数字和系数相乘的结果相加。
3. 用加出来和除以11，看余数只可能是：0－1－2－3－4－5－6－7－8－9－10，分别对应的最后一位身份证的号码为：1－0－X－9－8－7－6－5－4－3－2。即(余数+校验码)%11==1
4. 通过上面得知如果余数是2，就会在身份证的第18位数字上出现罗马数字的X（大写英文字母X）。如果余数是10，身份证的最后一位号码就是2。
用户输入一个身份证号，校验其是否是合法的身份证号码。
程序运行示例结果如下图所示：

220221197305166534
身份证号码校验为合法号码!

22022119730228653X
身份证校验位错误!

34052419800101001X
身份证号码校验为合法号码!

"""

# 先取所有数字到列表
id_ori = input()
id_lst = list(id_ori)
if id_lst[17] == 'X':
    id_lst[17] = 10
id_aut = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
id_che = []
for i in range(0, 17):
    id_che.append(int(id_lst[i]) * int(id_aut[i]))
id_lef = sum(id_che) % 11
if (id_lef + int(id_lst[17])) % 11 == 1:
    print('身份证号码校验为合法号码！')
else:
    print('身份证校验位错误！')
