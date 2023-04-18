from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Bark! Bark!"


class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"


animal1 = Dog()
animal2 = Cat()

print(animal1.speak())
print(animal2.speak())
