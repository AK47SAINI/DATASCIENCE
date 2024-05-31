class father:
    def hi(self):
        print("hi i am father")
class son(father):
    def hello(self):
        print("hi i am son")
obj=son()
obj.hi() #calling of the method of the parent class 
obj.hello()     
class daughter(father):
    def hey(self):
        print("hi i am daughter")
obj1=daughter()
obj1.hi()
obj1.hey()
