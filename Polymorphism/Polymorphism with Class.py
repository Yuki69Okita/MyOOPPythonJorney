class Dog:
    @staticmethod
    def speak():
        print("Bark! Bark!")


class Cat:
    @staticmethod
    def speak():
        print("Meow! Meow!")


class Cow:
    @staticmethod
    def speak():
        print("Muuuuuu!")


animal1 = Dog()
animal2 = Cat()
animal3 = Cow()

for animal in (animal1, animal2, animal3):
    animal.speak()
