class Dog:
    @staticmethod
    def speak():
        return "Bark! Bark!"


class Cat:
    @staticmethod
    def speak():
        return "Meow! Meow!"


def animal_speak(animal):
    print(animal.speak())


animal1 = Dog()
animal2 = Cat()

animal_speak(animal1)
animal_speak(animal2)
