class grandparent:
    def hi(self):
        print("we are grand parents")

class parent(grandparent):
    def hello(self):
        self.hi()
        print("we are parents")
class child(parent):
    def hey(self):
        self.hello()
        print("we are childs")


a=child()
a.hey()
