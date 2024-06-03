import numpy as np
import random
##SOLUTION OF THE FIRST PROBLEM OF THE ASSIGNMENT 4 (NUMPY)

arr=np.random.randint(0,100,(12,5))
# print(arr)
def func1(arr):
    arr1=arr[-1]
    print("Last row of the array is ",arr1)
    print("Average -> ",np.average(arr1))
    print("Minimum -> ",np.min(arr1))
    print("Maximum -> ",np.max(arr1))
    count=0

    for i in arr1:
        
       if i%2 == 0:
            count+=1
    print("No. of Evens -> ",count)
func1(arr)                          #CALLING OF FUNCTION func1()



##SOLUTION OF THE SECOND PROBLEM OF ASSIGNMENT 4 (NUMPY)
arr2=np.arange(1,10).reshape(3,3)
print("Original array \n",arr2)
print("After reversing the order \n",arr2[:,::-1]) ##TO REVERSE THE ORDER OF THE COLUMNS