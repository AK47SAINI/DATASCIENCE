# name=input("enter your name")
# age=int(input("enter your age"))
# print(f"name is {name} \nage is {age}")


# a=input("enter any alphabet")
# if a=='a'or a=='e' or a=='i' or a=='o' or a=='u' or a=='A' or a=='E' or a=='I' or a=='O' or a=='U':
#     print("alphabet is a vowel!")
# else:
#     print("alphabet is a consonent!") 
for i in "aashish":
    print(i)
for i in "aashish":
    print(i,end=" ")
name="aashish kumar saini"
for i in name:

    print(i)
num=20
for i in range(num):
    if(i%2==0):
        continue
    else:
        print(i,end=" ")
print() #for giving the gap of one line
l=["mango","apple","banana"]
for i in l:
    if(i=="banana"):
        break
    print(i)
num=20
#to print the range with the gap in between the elements
for i in range(0,num,2):
    print(i,end=" ")