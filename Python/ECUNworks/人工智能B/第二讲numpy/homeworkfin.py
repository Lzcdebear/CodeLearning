import numpy as np


print(np.reshape(np.arange(100,200,2),(5,10)))


print(np.reshape(np.random.randint(50,100,40),(5,8)))


print(np.arange(0,3.6,0.7))


print(np.random.normal(1.6,0.3,(3,5)))


print(np.eye(5,5))


l = np.array(L)


print(l[:,1])


print(l[1:3,2:5])


print(l[0:3:2,1::2])


a = np.array(l[2.5<=l])
print(np.array(a[a<=3.5]))



print(np.hstack((np.array(l[l>3]),np.array(l[l<0]))))

