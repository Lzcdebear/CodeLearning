﻿L1=[5,3,7,8,14,9,12,6]
s,psum=0,0
for v in range(L1):
    s+=v
psum+=v*v
s=s/len(L1)
mse=psum/len(L1)-s*s
print(f'方差为：{mse:.2f}')
