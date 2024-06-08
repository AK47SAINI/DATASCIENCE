import numpy as np

a=np.arange(1,17).reshape(4,4)
print("Given array is as follows:")

print(a)
print("The sum of the all elements of the array is ",np.sum(a))

print("The sum of the elements of each rows is ",np.sum(a,axis=1))
print("The sum of the elements of each colums is ",np.sum(a,axis=0))
