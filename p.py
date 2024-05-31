l=[3,5,3,3,6,4,5,0]

def diff(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
        else:
            continue
            
    return l1


print("different elements are",diff(l))