# l="green-yellow-white-blue-red"
l=input()
l1=[]
l1=l.split('-')
# print(l1)
l1.sort()
print("-".join(l1))