import math
import numpy as np
import pandas as pd

import pandas as pd
import numpy as np
title = ["公司","第一季度","第二季度","第三季度","第四季度"]
recs = [["Apple",51.9,57.9,48.7,50.4],["Samsung",69.7,64.6,41.7,51.7], \
["Huawei",31.7,58.6,59.2,47.9], ["Mi",41.7,38.6,58.0,58.9],["OPPO",69.8,31.1,58.7,30.4]]
phone =  pd.DataFrame(recs,index=range(1,6),columns=title)
print(phone)

print("DataFrame:\n", phone)   #输出DataFrame对象
print("Index:\n",phone.index)   #输出DataFrame对象的index属性
print("Columns:\n",phone.columns)  #输出DataFrame对象的columns属性
print("Values:\n",phone.values)   #输出DataFrame对象的values属性
print("公司:\n",phone.iloc[0:,0])  #以面向对象方式输出DataFrame对象的‘公司’列
print("Samsung公司第四季度的手机出货量:\n",phone.iloc[1,4])    #输出Samsung公司第四季度的手机出货量


