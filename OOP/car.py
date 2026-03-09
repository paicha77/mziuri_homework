class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        print(self.brand, self.model, self.year)


c = Car("BMW", "M5", 2022)
c.car_info()