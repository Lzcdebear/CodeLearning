a = input()
t = ''
for i in a:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        if 'a' <= i <= 'c' or 'A' <= i <= 'C':
            n = ord(i)
            n = n + 23
            t += chr(n)
        else:
            n = ord(i)
            n = n - 3
            t += chr(n)
print(t)
