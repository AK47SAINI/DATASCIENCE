import numpy as np

a=np.array(range(10,60,10))
print("Given array is as follows:")
print(a)
i=np.array([0,1,3])  #making an array of the indecies
# print(a[i])
a[i]=1,2,4 #assigning the new values to the a array using the index array i
print('After assigning the new values to the given indices of the array')
print(a)