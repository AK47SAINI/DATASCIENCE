#to print the table of the  any number
a=int(input("enter the number for printing the table"))
for i in range(1,11):
    print(f"{a} * {i} = ",a*i)

#ENUMERATE FUNCTION

a=["mango","apple","banana","berry"]
for index,i in enumerate(a):
    print(index," ",i)