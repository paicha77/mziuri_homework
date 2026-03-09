class Dog:
    def make_sound(self):
        print("Bark")


class Cat:
    def make_sound(self):
        print("Meow")


class Cow:
    def make_sound(self):
        print("Moo")


animals = [Dog(), Cat(), Cow()]

for a in animals:
    a.make_sound()