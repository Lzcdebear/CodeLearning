"""
python会先将字符串编码成为计算机能够识别的数据，然后通过解码再显示到显示屏上
"""
a = '天涯共此时'
b = 'nikco'
# GBK 和 UTF-8是两种不同的编码方式
# 其中 GBK 中一个中文字符占用两个位
# 其中 UTF-8 中一个中文字符占用三个位
print(a.encode(encoding='GBK'))
print(a.encode(encoding='UTF-8'))
print(b.encode(encoding='GBK'))
print(b.encode(encoding='UTF-8'))
# 在打印的时候前面会出现字母 b 表示的是二进制
byte1 = b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'  # GBK
byte2 = b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6'  # UTF-8
print(byte1.decode(encoding='GBK'))
print(byte2.decode(encoding='UTF-8'))
