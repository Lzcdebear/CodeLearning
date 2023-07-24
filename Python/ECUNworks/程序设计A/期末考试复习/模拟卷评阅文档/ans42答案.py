'''
评分标准

函数定义与返回处理正确：3分
函数体计算正确：3分

对所给数据列表循环处理正确：3分
函数调用和计算正确：3分

输入、输出处理正确：3分

'''
##参考答案1
Vaccines=[
    ['疫苗A',0.88,0.91,0.92,0.90,0.93],  
    ['疫苗B',0.85,0.89,0.91,0.90,0.88],   
    ['疫苗C',0.92,0.89,0.94,0.93,0.91],
    ['疫苗D',0.83,0.88,0.89,0.87,0.86],
    ['疫苗E',0.78,0.82,0.85,0.86,0.84]
]

def sceenVac(L,rate):
    outL=[]
    for v in L:
        if v>=rate:
            outL.append(v)
    return outL

rate=float(input("请输入需要筛选的有效率：\n"))

for vacc in Vaccines:  ##或其它方式循环遍历
    print('%s的结果:'%vacc[0],end='\t')  #或使用format格式输出
    
    result=sceenVac(vacc[1:],rate)
    if len(result)==0:
        print ("无")
    else:
        print (result)  
