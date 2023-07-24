# coding=utf-8
import pandas as pd
import numpy as np
'''
DataFrame对象是Pandas库的核心数据结构
它拥有跟表格极其相似的二维数据结构
它包括值（values）、行索引（index）和列索引（columns）三个部分。
'''

'''
 使用Pandas中的DataFrame ()函数创建DataFrame对象，其常用格式如下所示：

    pandas.DataFrame(data, index, columns,…)

data包含了DataFrame对象中存储的数据,data的类型可以是NumPy的二维数组或列表等可迭代对象；
index包含了DataFrame对象中存储数据对应的行索引值，如果省略，则自动生成0 - n-1的整数行索引值，n为data中元素的行数；
columns包含了DataFrame对象中存储数据对应的列索引值，如果省略，则自动生成0 - m-1的整数列索引值，m为data中元素的列数。
'''
iris=pd.DataFrame([[5.1,3.5,1.4],[4.9,3.0,1.4],[4.7,3.2,1.3]],index=[1,2,3],
columns=['sepal length (cm)','sepal width (cm)','petal length (cm)'])
print(iris)


'''
(1)DataFrame中元素的访问
  DataFrame对象和Series对象一样，既可以通过位置索引来访问，也可以通过行列索引名来访问。

DataFrame[ ]：使用列索引名或列索引名列表得到某列或某几列。
DataFrame.loc[index,columns]：使用行、列索引或索引列表获取查询区域值。
DataFrame.iloc[iloc,cloc]：使用行、列位置索引或位置索引列表获取查询区域值。
'''

'''
#使用列索引名访问一列，得到Seires对象 
'''
print(iris['sepal length (cm)'])

'''
#使用列索引名列表访问多列，得到DataFrame对象
'''
print(iris[['sepal length (cm)','petal length (cm)']])

'''
#使用行、列索引名，得到一个表格元素
'''
print(iris.loc[1,'sepal length (cm)'])

'''
#使用:，获取指定列所有元素，得到Seires对象
'''
print(iris.loc[:,'sepal length (cm)'])

'''
#使用行索引名切片，列索引名列表，得到DataFrame对象
'''
print(iris.loc[2:,['sepal length (cm)','petal length (cm)']])

'''
#使用位置索引切片，位置索引列表，得到DataFrame对象
'''
print(iris.iloc[2:,[0,2]])

'''
(2)DataFrame中元素的条件查询
  和NumPy模块一样，通过布尔运算方式可以获得逻辑值列表，
    DataFrame的访问中，逻辑值列表可以出现在索引的位置，实现筛选。
'''
# 布尔运算获得逻辑值列表
print(iris['sepal width (cm)']>3.0)

# 在[]访问方式中使用逻辑值列表，得到符合条件的所有列的元素构成的DataFrame对象
print(iris[iris['sepal width (cm)']>3.0])

# 在loc[]访问方式中使用逻辑值列表，得到符合条件的指定列的元素构成的DataFrame对象
print(iris.loc[iris['sepal width (cm)']>3,["sepal length (cm)",  "sepal width (cm)"]])


'''
(3)DataFrame中元素的增加
调用append()函数进行行的添加
append()函数用于将新的行增加到DataFrame的末尾，并返回新的对象，同时该函数不会改变原始对象，其格式如下：
    DataFrame.append(other, ignore_index=False,…)
其中，other包含了需要增加的数据
other的类型可以是DataFrame、Series、字典等。
ignore_index参数设置是否使用原来的行索引，默认为使用，设置为True则不使用，生成的新的DataFrame对象使用默认的行索引值。
'''
# 为新行创建一个新的DataFrame对象，追加到iris对象，返回一个新的DataFrame对象
data1 = pd.DataFrame([[4.6,3.1,1.5]],index=[4],columns = ['sepal length (cm)','sepal width (cm)','petal length (cm)'])
irisnew = iris.append(data1)
print(irisnew)

# 为新行创建一个字典对象，追加到iris对象，返回一个新的DataFrame对象
data2={'sepal length (cm)':4.6,'sepal width (cm)':3.1,'petal length (cm)':1.5}
irisnew=iris.append(data2,ignore_index=True)
print(irisnew)

'''
通过赋值进行列的添加
  向DataFrame对象的增加新列，类似字典操作，通过列索引名访问一列，如果列索引名是新值，进行赋值，就可以完成DataFrame中列的添加。
'''
iris['petal width (cm)']=[0.2,0.2,0.2]  # 将索引值'petal width (cm)'对应的元素列赋值为[0.2,0.2,0.2]
print(iris)


'''
4)DataFrame中元素的删除
  drop()函数表示从DataFrame中删除单个或多个行（列）索引值对应的元素，并返回删除元素后的DataFrame，该函数在默认情况下不修改原始对象，其格式如下：

    DataFrame.drop(labels=None, axis=0, inplace=False,…)

其中，
labels  表示索引名或多个索引名组成的列表，如无索引名，可提供位置索引；
axis    表示删除行或者列，值为0表示删除行，labels参数为行索引名或表示行索引名列表，值为1表示删除列，labels参数为列索引名或列索引名列表；
inplace 表示是否对当前对象进行改变，值为False表示当前对象不改变，生成新对象，值为True表示操作当前对象，直接删除，不产生新对象。
'''
iris=pd.DataFrame([[5.1,3.5,1.4],[4.9,3.0,1.4],[4.7,3.2,1.3]],index=[1,2,3],columns=['sepal length (cm)','sepal width (cm)','petal length (cm)'])
iris['petal width (cm)']=[0.2,0.2,0.2]  # 将索引值'petal width (cm)'对应的元素列赋值为[0.2,0.2,0.2]

# 删除iris对象中行索引值为1和2的元素，返回新对象iris_new
iris_new=iris.drop([1,2],axis=0)
print(iris_new)

# 直接删除iris_new对象中的'petal length (cm)'和'petal width (cm) '两列
iris_new.drop(['petal length (cm)','petal width (cm)'],axis=1,inplace=True)
print(iris_new)

'''
(5)DataFrame中元素的修改
  DataFrame对象的数据列支持Python支持的常见算术运算，如：“+”，“-”，“*”，“/”等。
    通过赋值语句修改数据，可以修改指定行列记录的数据，还可以把要修改的数据查询筛选出来，重新赋值。
'''
# 将"petal width (cm)" 列的值赋值为0.3
iris["petal width (cm)"]=0.3
print(iris)
iris.loc[iris["sepal length (cm)"]<5,"petal width (cm)"]-=0.2
print(iris)


'''
3. 数据文件读写
  人工智能数据的来源多种多样，因此Pandas提供了多种格式数据的导入和导出，包括CVS、Excel、JSON、SQL、TXT和HTML等格式。本节将介绍CSV和Excel文件的数据读写方法。

（1）读写CSV文件
  CSV（Comma-Separated Value）是一种以纯文本形式存储表格数据的文本文件，通常使用逗号作为字符之间的间隔符。Pandas对其提供了相应的读写功能。

从CSV文件读取数据到DataFrame对象
  read_csv()函数用于将数据从CSV文件读取到DataFrame对象，其常用格式如下：

    pandas.read_csv(filepath_or_buffer,…)

  其中，filepath_or_buffer的类型为字符串，包含了文件路径和文件名。
'''
# 从CSV文件读取数据到DataFrame对象
iris=pd.read_csv(r'F:\Python\ECUNworks\人工智能B\第三讲pandas\Iris_pandas.xlsx')
print(iris)

'''
从DataFrame对象写入数据到CSV文件
  to_csv()函数用于将数据从DataFrame对象写入到CSV文件，其格式如下：

    DataFrame.to_csv(path_or_buf,…)

  其中，path_or_buf的类型为字符串，包含了文件路径和文件名。
'''
# 从DataFrame对象写入数据到CSV文件
iris.to_csv(r'C:\\配套资源\\第4章\\Iris_pandas_new.csv')
