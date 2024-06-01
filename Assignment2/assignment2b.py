class discount:
    def calculate_discount(self,original_price,discount_percentage):
    
        return original_price-original_price*(discount_percentage/100)


a=discount()
orig_price=float(input("Enter the Original Price of the item : "))
disc_percent=float(input("Enter the discount percentage : "))

print("Final price of the item after applying the discounts is : ",a.calculate_discount(orig_price,disc_percent),"Rupees")