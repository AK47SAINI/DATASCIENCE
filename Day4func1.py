#FUNCTIONS WITH THE PARAMETERS
def sum(a,b):
    return a+b


print("sum of the given values is ",sum(2,4))
def mul(a=12,b=2): #function with the predefined/default parameters 

    return a*b

print("multiplication of the given values is ",mul(2,6))


def swap(a,b):
    return b,a
print("swap of the values is ",swap(4,5))

#FUNCTION WITHOUT OF THE PARAMETERS
def hello():
    print("hello i am Aashish")
hello()


def myfunc(name):
    print(name,"kumar saini")

myfunc("ashish")