def fact(n):
    ret = 1
    for i in range(2,n+1):
        ret *= i
    return ret

n = int(input())

l = []

for i in range(1, n+1):
    l.append(fact(i))

print(sum(l))
