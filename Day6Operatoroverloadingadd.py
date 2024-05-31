#operatoroverloading
#for more details https://www.geeksforgeeks.org/operator-overloading-in-python/

class Main:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,o):
        return self.a+o.a,self.b+o.b

A=Main(3,4)
B=Main(4,5)
C=A+B
print("sum of A and B obj is ",C)