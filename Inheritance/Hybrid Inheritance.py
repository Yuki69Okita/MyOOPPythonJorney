class Animal:
    def __init__(self, kind):
        self.kind = kind


class Breed(Animal):
    def __init__(self, kind, breed):
        Animal.__init__(self, kind)
        self.breed = breed


class Dog(Breed):
    def __init__(self, name):
        self.name = name
        Breed.__init__(self, "French Bulldog", "Mammal")


class Bird(Breed):
    def __init__(self, name):
        self.name = name
        Breed.__init__(self, "Songbird", "Bird")


dog1 = Dog("Lizzy")
print(f"Name: {dog1.name}, Breed: {dog1.breed}, Kind: {dog1.kind}")

bird1 = Bird("JoJo")
print(f"Name: {bird1.name}, Breed: {bird1.breed}, Kind: {bird1.kind}")

