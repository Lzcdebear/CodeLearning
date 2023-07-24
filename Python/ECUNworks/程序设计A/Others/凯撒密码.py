s1 = 'abcdefghijklmnopqrstuvwxyz'
s2 = 'xyzabcdefghijklmnopqrstuvw'
upper_s1 = s1.upper()
upper_s2 = s2.upper()
txt = input()
miwen = []
for ch in txt:
    if ch in s1:
        idx = s1.index(ch)
        miwen.append(s2[idx])
    elif ch in upper_s1:
        idx = upper_s1.index(ch)
        miwen.append(upper_s2[idx])
    else:
        miwen.append(ch)

result = "".join(miwen)
print(result)