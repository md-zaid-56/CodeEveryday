class Product:
    def __init__(self,name,price,stock):
        self.name = name #Public
        self._price = price #Protected
        self.__stock = stock #Private

    def display_product(self):
        print("="*21)
        print(f"Product Name:{self.name}\nProduct Price:{self._price}\nProduct InStock:{self.__stock}\n")
        print("="*21)

product1 = Product("Laptop", 75000, 10)
product1.display_product()
product1.name = "PC" #The Name will be changed because it is using access Specifier as PUBLIC
product1._price = 5000 #This will also change because the access specifier used in this is PROTECTED , it doesn't restrict
product1.__stock = 50 #This will doesn't Modify because the access specicfier used in this is PRIVATE , it will just perform "name mangling"
#product1._Product__stock = 50 #This will modify the stock because we used name mangling
product1.display_product()