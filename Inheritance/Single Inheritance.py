class Dog:
    def __init__(self, is_cute, size):
        self.is_cute = is_cute
        self.size = size


class FrenchBulldog(Dog):
    def __init__(self, name):
        self.name = name
        self.breed = "French Bulldog"
        Dog.__init__(self, True, "Small")


dog1 = FrenchBulldog("Lizzy")
print(f"Name: {dog1.name}, Cute: {dog1.is_cute}, Breed: {dog1.breed}, Size: {dog1.size}")

dog2 = FrenchBulldog("JoJo")
print(f"Name: {dog2.name}, Cute: {dog2.is_cute}, Breed: {dog2.breed}, Size: {dog2.size}")
