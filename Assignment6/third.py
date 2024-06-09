import numpy as np
a=np.arange(1,61,1).reshape(3,4,5)
print(a)
print("The last 2 rows of the last 2 matrix are as follows:")

print(a[1:,-2::1,:])
print("The last 2 columns of the last 2 matrices are as follows:")
print(a[1:,:,-2::1])