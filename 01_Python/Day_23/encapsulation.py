class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display_product(self):
        print("="*21)
        print(f"Product Name:{self.name}\nProduct Price:{self.price}\nProduct InStock:{self.stock}\n")
        print("="*21)

    def add_stock(self,quantity):
        if quantity <= 0:
            print("Please Enter Valid Quantity")
            return
        self.stock += quantity
        print("="*21)
        print(f"Stock Added in {self.name}:{quantity}")
        print("="*21)

    def sell(self,quantity):
        if quantity <= 0:
            print("Please Enter Valid Quantity")
            return

        if quantity > self.stock :
            print(f"Not Sufficient in Stock available in stock are {self.stock}")
            return

        self.stock -= quantity
        print("="*21)
        print(f"Stock sold of {self.name}:{quantity}")
        print("="*21)

product1 = Product("Laptop", 75000, 10)

product1.display_product()

product1.add_stock(5)

product1.sell(3)

product1.display_product()