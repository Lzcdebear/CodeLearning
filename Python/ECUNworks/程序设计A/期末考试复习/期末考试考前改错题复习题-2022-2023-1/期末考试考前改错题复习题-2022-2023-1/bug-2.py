s=input("请输入一个字符串:\n")
s2 = s.lower()
fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
for c in s2:
    if  c in fomart:
        s = s.replace(c,'')
print("只保留英文和数字后的字符串为："+s2)
