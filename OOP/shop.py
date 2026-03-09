class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount):
        if amount > self.quantity:
            print("Not enough products")
        else:
            self.quantity -= amount

    def restock(self, amount):
        self.quantity += amount

    def product_info(self):
        print(self.name, self.price, self.quantity)


p = Product("Apple", 2, 50)
p.buy(10)
p.restock(20)
p.product_info()