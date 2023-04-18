class Animal:
    def __init__(self, kind):
        self.kind = kind


class Size(Animal):
    def __init__(self, kind, breed):
        Animal.__init__(self, kind)
        self.breed = breed


class Dog(Size):
    def __init__(self, name):
        self.name = name
        Size.__init__(self, "Mammal", "Small")


dog1 = Dog("Lizzy")
print(f"Name: {dog1.name}, Size: {dog1.breed}, Kind: {dog1.kind}")

dog2 = Dog("JoJo")
print(f"Name: {dog2.name}, Size: {dog2.breed}, Kind: {dog2.kind}")
