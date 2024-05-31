# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("name is",self.name)
#         print("age is ",self.age)

# a=student("aashish",21)
# a.display()
# b=student("ram",22)
# b.display()


class animal:
    num1=34
    num2=35
    def __init__(self,name,weight,age):
        self.name=name
        self.age=age
        self.weight=weight
    def display(self):
        print("Animal name is",self.name)
        print("age is",self.age)
        print("age is",self.age)
        print("age is",self.age)
        print("age is",self.age)

        print("weight is",self.weight)
a=animal("dog","10kg",4)
a.display()
b=animal("cat","7kg",3)
b.display()
print(a.num1) #we can access the default variable by object

print(animal.num1) #also access by the classname.defaultvariable
