#ans42.py

Vaccines=[
    ['疫苗A',0.88,0.91,0.92,0.90,0.93],
    ['疫苗B',0.85,0.89,0.91,0.90,0.88],   
    ['疫苗C',0.92,0.89,0.94,0.93,0.91],
    ['疫苗D',0.83,0.88,0.89,0.87,0.86],
    ['疫苗E',0.78,0.82,0.85,0.86,0.84]
]

def screenVac(vac, thd):
    #vac -->[0.88,0.91,0.92,0.90,0.93]
    result = []
    for x in vac:
        if x >= thd:
            result.append(x)
    return result


threshold = input('请输入需要筛选的有效率：\n')
threshold = float(threshold)

for item in Vaccines:
    name = item[0]
    data = item[1:]
    ret = screenVac(data,threshold)
    if len(ret) > 0 :
        print(f'{name}的结果:\t{ret}')
    else:
        print(f'{name}的结果:\t无')
    
