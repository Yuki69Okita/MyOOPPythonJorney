class Animal:
    def __init__(self, kind):
        self.kind = kind


class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.breed = "French Bulldog"
        Animal.__init__(self, "Mammal")


class Bird(Animal):
    def __init__(self, name):
        self.name = name
        self.breed = "Songbird"
        Animal.__init__(self, "Bird")


dog1 = Dog("Lizzy")
print(f"Name: {dog1.name}, Breed: {dog1.breed}, Kind: {dog1.kind}")

bird1 = Bird("JoJo")
print(f"Name: {bird1.name}, Breed: {bird1.breed}, Kind: {bird1.kind}")
