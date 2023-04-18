class Animal:
    def __init__(self, kind):
        self.kind = kind


class Size:
    def __init__(self, size):
        self.size = size


class Dog(Animal, Size):
    def __init__(self, name):
        self.name = name
        Animal.__init__(self, "Mammal")
        Size.__init__(self, "Small")


dog1 = Dog("Lizzy")
print(f"Name: {dog1.name}, Size: {dog1.size}, Kind: {dog1.kind}")

dog2 = Dog("JoJo")
print(f"Name: {dog2.name}, Size: {dog2.size}, Kind: {dog2.kind}")
