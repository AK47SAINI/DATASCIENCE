

##STRINGS##

name="   aashish kumar saini  "
print(name)
print(name.lower())
print(name.upper())
print(name.split())
print(name[1:6])
print(name.rstrip())
print(name.lstrip())
print(name.strip())
name='aashish'
print(name[:])
print(name[:5])
print(name[0:])
print(name[:7:2])
print(name[-1:-7:-1])
n="aashsish \"kumar\"saini"

print(n)
a="hello"
b="world"
c=a+b
d=a+" "+b
print(c)
print(d)
print(' '.join([a,b])) #it take only the list and joined it

#formatted strings
print(f"{a} {b}")

##BOOLEAN##

a=True
print(a)
if(a):
    print("aashish")
b=False
if(b):
    print("hello ")

if(not b):
    print("hello")

    ##LIST##
    l=["aashish","kumar","saini"]
    print(l)
    for i in l:
        print(i)
print("length of the string is :",len(l))
print(" ".join(l))
l2=["aashish",'2','3']
print(" ".join(l2))
    


l2[0:2]="aaasish"
print(l2)

l1=["aashish","kumar"]

l2=["saini"]
l1.extend(l2)
print(l1)
l1.clear()

print(l1)
num=[3,5,36,7,1,7,0,3]
print(sorted(num))
num.sort()
print(num)
print(sorted(num,reverse=True))

