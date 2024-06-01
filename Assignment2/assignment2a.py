class area:



    def calculate_area(self,radius):  #function to calculate the area of the circle that takes the radius as input
        
        return radius*radius*3.14
a=area()
r=float(input("Enter the radius of the circle : "))  #taking the radius from the user as input
area=a.calculate_area(r)
print("The area of the circle is :",area)