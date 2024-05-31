#LAMBDA FUNCTIOON
cube=lambda x:x*x*x
print("cube of the given number is ",cube(4))
mul=lambda x,y:x*y
print("multiply of the given function is ",mul(4,5))
sum=lambda x,y,z:x+y+z
print("sum of three number is ",sum(4,5,6))
def myfunc(n):

    return lambda a:a*n
double=myfunc(2) #the double is act as the lambda function and 
# it gets the value of the n from the function
print("double of the given number is ",double(4))
def t(n): #it also can be take double arguments from the lambda function
    return lambda x,y:n*x*y
ta=t(3)
print(ta(5,4))
