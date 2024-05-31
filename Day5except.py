##EXCEPTION HANDLING##

try:
    

    a=int(input("enter first number"))



    b=int(input("enter second number"))
    print("program in running ")

  
    div=a/b
    print("answer is ",div)

except Exception as e:
    print("error occurred is as follows \n",e)
else:
    print("no exception found")
finally:
    print("your code is executed successfully")