class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Bark! Bark!"


class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"


animals = [Dog("Ricky"), Cat("Alex")]

for animal in animals:
    print(f"{animal.name} says {animal.make_sound()}")
