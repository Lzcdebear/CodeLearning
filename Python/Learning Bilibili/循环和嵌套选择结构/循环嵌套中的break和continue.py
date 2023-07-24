# 这里展示的是break和continue在循环结构中的使用方式和效果
"""
break和continue都是只能适用在循环结构中的，它们控制的也只有循环结构
如果在分支结构中出现break，不仅会跳出分支结构，还会跳出分支结构之外的循环结构
"""
# 这里先展示break的效果
for i in range(5):
    for j in range(1,11):
        if j % 2 ==0:
            break
        print(j, end='\t')
    print()
# 这里再来展示continue的效果
for i in range(5):
    for j in range(1,11):
        if j % 2 ==0:
            continue
        print(j, end='\t')
    print()
