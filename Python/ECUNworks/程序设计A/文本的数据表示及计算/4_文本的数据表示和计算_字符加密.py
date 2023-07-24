a = input()
lst = list(a)
i = len(lst)
j = 0
p = ''
while j < i:
    if 'a' <= lst[j] <= 'z' or 'A' <= lst[j] <= 'Z':
        if 'x' <= lst[j] <= 'z' or 'X' <= lst[j] <= 'Z':
            n = ord(lst[j])
            n = n - 23
            lst[j] = chr(n)
        else:
            n = ord(lst[j])
            n = n + 3
            lst[j] = chr(n)
    j += 1
for h in lst:
    p += str(h)
print(p)
