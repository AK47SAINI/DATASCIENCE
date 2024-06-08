import numpy as np
a=np.arange(1,61,1).reshape(3,4,5)
print(a)
print(a[1:,-2::1,])