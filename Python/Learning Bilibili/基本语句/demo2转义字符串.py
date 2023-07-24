# 本文档是转义字符串使用方法
print('hello\nworld')
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')
print('hello\bworld')

print('http:\\www.baidu.com')
# 只有一个斜线，因为\\为输出一个\
print('http:\\\\www.baidu.com')
# 输出两个斜线
print('老师说:\'fuck you man\'')
# 在字符串中输出‘’的方法

# 如果不想使得转义字符产生作用，则在字符串前面加上r或则R
print(r'hello\nworld')
# 最后一个字符不可以是反斜线\,但是可以是\\表示输出\
