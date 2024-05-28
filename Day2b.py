l=["aashish",'rizwan',"sachin","ajay"]
print(sorted(l))
l.sort()
##key=str.lower() if the strings are in different cases
#if the 
l.reverse()
print(l)
print(l.count("aashish")) ##for counting the count of the any element in the list we use the count function



#tuple

t1=(2,5,6,3,5)
t2=()
print(type(t1))


print(type(t2))
print(t1)
t2=('aashish',3,6,'kumar','saini')
print(t2)
print("length of the second tuple is ",len(t2))
t3=("aashishh")
print(type(t3))
t3=("aashish",)
print(type(t3))
#for changing the data of the tuple first we have to convert it into the 
#list then we can modify the data of the list and thenn we can convert it to the tuple again
t2l=list(t2)
t2l[0]='aa'
t2=tuple(t2l)
print(t2)
print(type(t2))
