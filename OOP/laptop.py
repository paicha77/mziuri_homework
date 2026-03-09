class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

    def laptop_info(self):
        print(self.brand, self.ram, self.price)


l = Laptop("Lenovo", "16GB", 1200)
l.laptop_info()