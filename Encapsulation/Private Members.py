class MyClass:
    def __init__(self):
        self.x = 10
        self.__y = 3

    @staticmethod
    def public_method():
        print("Public.")

    @staticmethod
    def __private_method():
        print("Private.")


obj1 = MyClass()

print(obj1.x)
print(obj1.__y)

obj1.public_method()
obj1.__private_method()

