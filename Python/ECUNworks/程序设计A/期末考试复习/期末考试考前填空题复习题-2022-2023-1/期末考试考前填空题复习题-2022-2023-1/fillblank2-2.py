dic={'001':80,'002':90,'003':100,'004':70,'005':60}
while True:
    print("请选择功能：\n1: 修改分数\n2：查看分数\n3：计算总分\n0:退出")
    c=input()
    if __________:
        stuno=input("请输入要修改分数的学号（按回车结束）：")
        if stuno in dic:
            score=int(input("请输入分数："))
            dic[stuno]=score
            print("该学生分数已修改。")
        else:
            print("库中未找到这个学生")
    elif c=="2":
        stuno=input("请输入要查询的学号（按回车结束）：")
        if stuno in dic:
            print("%s的分数是%d"%(___________))
        else:
            print("库中未找到这个学生")
    elif c=="3":
        s=_______
        for x in dic.keys():
            s=s+dic[x]
        print(s)
    elif c=="0":
        _________
    _________:
        print("输入有误！")
