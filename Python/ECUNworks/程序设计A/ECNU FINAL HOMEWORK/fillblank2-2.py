dic={'001':80,'002':90,'003':100,'004':70,'005':60}
while True:
    print("请选择功能：\n1: 修改分数\n2：查看分数\n3：计算总分\n0:退出")
    c=input()
    if c==1:
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
            print("%s的分数是%d"%(stuno, dic[stuno]))
        else:
            print("库中未找到这个学生")
    elif c=="3":
        s=0
        for x in dic.keys():
            s=s+dic[x]
        print(s)
    elif c=="0":
        break
    else:
        print("输入有误！")


"""
要求：字典中已记录学号001-005的同学分数，完善程序，实现按学号修改分数、按学号查看分数、计算总分的功能。
"""