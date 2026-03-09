class Ticket:
    def __init__(self, title, ticket_price, ticket_raodenoba, language = "geo"):
        self.title = title
        self.ticket_price = ticket_price
        self.ticket_raodenoba = ticket_raodenoba
        self.language = language

    def __str__(self):
        print("movie ragaca")

    def __lt__(self, other):
        other = self.ticket_raodenoba
        if self.ticket_raodenoba < other:
            print(f'{self.ticket_raodenoba} is less then {other}')
        if self.ticket_raodenoba <= 10:
            print("u can buy this")



class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def __str__(self):
        print(self.name, self.balance)

    def deposit(self, amount):
        self.balance += amount










movie1 = Ticket("titanic", 20, 10)
movie2 = Ticket("catch me if you can", 30, 9)
user1 = User("nika", 100)





