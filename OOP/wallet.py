class Wallet:
    def __init__(self, money):
        self.__money = money

    def add_money(self, amount):
        self.__money += amount

    def spend_money(self, amount):
        if amount > self.__money:
            print("Not enough money")
        else:
            self.__money -= amount

    def see_money(self):
        return self.__money


w = Wallet(100)
w.add_money(50)
w.spend_money(30)
print(w.see_money())