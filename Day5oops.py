##OOPS##
class student:
    def get(self,name,age):
        self.name=name
        self.age=age
    def put(self):
        print("name is ",self.name)
        print("age is ",self.age)
a=student()
a.get('aashish',22)
a.put()