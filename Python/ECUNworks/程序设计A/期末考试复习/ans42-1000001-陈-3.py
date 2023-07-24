#ans42.py

Vaccines=[
    ['疫苗A',0.88,0.91,0.92,0.90,0.93],
    ['疫苗B',0.85,0.89,0.91,0.90,0.88],   
    ['疫苗C',0.92,0.89,0.94,0.93,0.91],
    ['疫苗D',0.83,0.88,0.89,0.87,0.86],
    ['疫苗E',0.78,0.82,0.85,0.86,0.84]
]

def screenVac(vac, thd):
    #vac -->['疫苗A',0.88,0.91,0.92,0.90,0.93]
    lst = []
    for i in range(1,len(vac)):
        x = vac[i]
        if x >= thd:
            lst.append(x)
    return [vac[0],lst]


threshold = input('请输入需要筛选的有效率：\n')
threshold = float(threshold)

for item in Vaccines:
    ret = screenVac(item,threshold)
    #print(ret)
    
    if len(ret[1]) > 0 :
        print(f'{ret[0]}的结果:\t{ret[1]}')
    else:
        print(f'{ret[0]}的结果:\t无')
    
