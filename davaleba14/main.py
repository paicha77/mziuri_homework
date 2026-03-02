# N1
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 2500:
            print("არ შეიძლება 2500 ლარზე მეტი თანხის შეტანა.")
        elif amount <= 0:
            print("შეიყვანეთ სწორი თანხა.")
        else:
            self.balance += amount
            print(f"თანხა წარმატებით დაემატა. მიმდინარე ბალანსი: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("შეიყვანეთ სწორი თანხა.")
        elif amount > self.balance:
            print("ანგარიშზე საკმარისი თანხა არ არის.")
        else:
            self.balance -= amount
            print(f"თანხა წარმატებით ჩამოიჭრა. მიმდინარე ბალანსი: {self.balance}")

    def display_balance(self):
        print(f"მიმდინარე ბალანსი: {self.balance}")


# N2
class Shape:
    def describe(self):
        print("I am a shape")


class Polygon(Shape):
    def __init__(self, sides):
        self.sides = sides


class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__(3)
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return area


triangle = Triangle(3, 4, 5)
triangle.describe()
print("Triangle area:", triangle.calculate_area())