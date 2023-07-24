# ans22_lzc.py
import string

str1 = input("请输入一个字符串：\n")
s = [str1]
for ch in str1:
    if ch in string.punctuation:
        continue
    else:
        s += ch
print(s)
