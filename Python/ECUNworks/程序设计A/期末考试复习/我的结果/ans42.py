# ans42.py

Vaccines = [
    ['疫苗A', 0.88, 0.91, 0.92, 0.90, 0.93],
    ['疫苗B', 0.85, 0.89, 0.91, 0.90, 0.88],
    ['疫苗C', 0.92, 0.89, 0.94, 0.93, 0.91],
    ['疫苗D', 0.83, 0.88, 0.89, 0.87, 0.86],
    ['疫苗E', 0.78, 0.82, 0.85, 0.86, 0.84]
]


def screenVac(a):
    vacdata = Vaccines
    vacreqe = a
    vacall = []
    for i in vacdata:
        name = str(i[0])
        vacpass = [name]
        leg = len(i)
        for j in range(1, leg):
            if float(i[j]) >= vacreqe:
                vacpass.append(i[j])
        vacall.append(vacpass)
    return vacall


x = float(input('请输入需要筛选的有效率：'))
vacres = screenVac(x)
for i in vacres:
    nam = i[0]
    i.pop(0)
    res = i
    if res:
        print(nam, '的结果:\t', res)
    else:
        print(nam, '的结果:\t无')
