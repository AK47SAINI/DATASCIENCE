class Father:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("constructor is executed")
    def display(self):
        print("father name",self.name)
        print("father age",self.age)
class Son(Father):
    def son_hi(self):
        print("hi i am son")
        print("i am 22 year old")

a=Son("ashish",43)  #by the help of the derived class object we can call the base class's constructors

a.display()
a.son_hi()
