a = str(input())
dict1 = {}
max_key = 0
b = 0
for i in a:
    dict1[i] = dict1.get(i, 0) + 1
for i in a:
    a = dict1.get(i)
    if b < a:
        b = a
        max_key = i
print(max_key, b)
