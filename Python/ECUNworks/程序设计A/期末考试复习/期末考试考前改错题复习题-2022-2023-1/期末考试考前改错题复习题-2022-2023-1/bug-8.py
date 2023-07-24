def isNarcissus(num):
     val = False
     a=num//10 #个位数
     c=num//100 #百位数
     b=num//10-c*10 #十位数
     if (num = a**3+b**3+c**3):
          val = True
     return val

for n in range(100,1000):
     if (!isNarcissus(n)):
          print(f"{n}是一个水仙花数")
