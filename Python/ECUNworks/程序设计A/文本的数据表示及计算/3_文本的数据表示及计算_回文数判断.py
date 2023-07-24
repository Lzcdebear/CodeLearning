x = input()
a = str(x)
a = list(a)
for i in a:
    if i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and \
            i != '9' and i != '0' and i != '-':
        print('输入的不是自然数！')
        break
    else:
        g = float(x)
        p = g % 1
        if p != 0 or g < 0:
            print('输入的不是自然数！')
            break
        elif 10000 <= g <= 99999:
            lst1 = list(x)
            lst2 = lst1[::-1]
            b = str(lst2)
            a = str(lst1)
            if b == a:
                print(x, '是回文数', sep='')
                break
            else:
                print(x, '不是回文数', sep='')
                break
        else:
            print('输入长度错误！')
            break
