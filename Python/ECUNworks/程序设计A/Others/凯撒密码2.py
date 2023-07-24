txt = input()
miwen = []
for ch in txt:
    if ch == 'a' or ch == 'b' or ch == 'c':
        code = ord(ch) + 26 -3
        mima = chr(code)
        miwen.append(mima)
    elif ch == 'A' or ch == 'B' or ch == 'C':
        code = ord(ch) + 26 -3
        mima = chr(code)
        miwen.append(mima)
    else:
        code = ord(ch) -3
        mima = chr(code)
        miwen.append(mima)

result = "".join(miwen)
print(result)