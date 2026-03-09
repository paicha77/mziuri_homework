class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount

    def show_health(self):
        print(self.name, self.health)


p = Player("Hero", 100)
p.take_damage(20)
p.heal(10)
p.show_health()