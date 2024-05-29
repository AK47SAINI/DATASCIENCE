i=0
while i<20:
    print(i,end=" ")
    i+=1


j=0
while j<40:
    if j%2==0:
        print(j)
    
    if j==20:
        break
    j+=1

k=0
while k<6:
    k+=1   #increement in the values should be before the continue
    if(k==2):
        continue
    else:
        print(k)