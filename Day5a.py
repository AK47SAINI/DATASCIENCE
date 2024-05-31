class Bank:
    name="raju rastogi"
    address="mumbai"
    age=22
    bankname="laxmi chit fund"
    accname=2484404004
    def display(self):
        print("Bank name is ",self.bankname)
        print("Account holder name",self.name)
        print("Account number is",self.accname)

        print("age is",self.age)
        print("address is",self.address)
a=Bank()
a.display()
a.name="ashish"
a.display()

b=Bank()
