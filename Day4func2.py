# #FUNCTION THAT RECEIVES THE MULTIPLE ARGUMENTS AND RECEIVED IN THE POINTER
# def myfunc(*name):  
#     for i in name:
#         print(i,end=" ")
#     print()
#     print("the youngest child is",name[1])


# myfunc("aashish","sahil","sachin","ram","shyam")
# def sqr(num):
#     for i in num:
#         print(i*i)
# print("enter total quantity of the square number")
# n=int(input())
# l=list()
# for i in range(n):
#     l1=int(input())
#     l.append(l1)

# print("Square of the given number are as follows \n ")
# sqr(l)
# def square(list1):
#     temp=[]
#     for x in list1:
#         temp.append(x**2)
#     return temp

# output=square([2,3,4,5])
# print(output)
#function to print average
# def avg(l):
#     n=len(l)
#     s=sum(l)
#     return s/n
# print(avg([2,3,2]))


a=[2,4,5,7,7,2,9,0]


#function ot print the minimum value from the list

def minimum(a):
    min=a[0]
    for i in a:
        if i<min:
            min=i
    return min
print("minimum value is",minimum(a))
def maximum(a):
    max=a[0]
    for i in a:
        if i>max:
            max=i
    return max
print("maximum value is",maximum(a))


