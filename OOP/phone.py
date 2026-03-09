class Phone:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    def use_battery(self, amount):
        self.battery -= amount

    def charge(self, amount):
        self.battery += amount

    def show_battery(self):
        print(self.battery)


p = Phone("Samsung", 100)
p.use_battery(20)
p.charge(10)
p.show_battery()