class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance")
        else:
            self.balance -= amount

    def display_balance(self):
        print(self.balance)


acc = BankAccount("Nika", 500)
acc.deposit(200)
acc.withdraw(100)
acc.display_balance()