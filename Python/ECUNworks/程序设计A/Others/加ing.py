txt=input("请输入字符串：") 
if len(txt) < 3 :
    print(txt)
else:    
    s1 = txt[-3:]
    if s1 == 'ing':
        txt = txt + "ly"
        print(txt)
    else:
        txt = txt + "ing"
        print(txt)
    

