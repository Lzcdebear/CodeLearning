ls = ( 7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2 )
id = input()
sum = 0
for i in range(17):
    sum = sum + ls[i] * int(id[i])
if str(id[17]) == 'X':
    if sum % 11 == 2:
        print('身份证号码校验为合法号码!')
    else:
        print('身份证校验位错误!')
elif (sum % 11 + int(id[17])) % 11 == 1:
    print('身份证号码校验为合法号码!')
else:
    print('身份证校验位错误!')
