class MyClass:
    def __init__(self):
        self.x = 10
        self._y = 3

    @staticmethod
    def public_method():
        print("Public.")

    @staticmethod
    def _protected_method():
        print("Protected.")


obj1 = MyClass()

print(obj1.x)
print(obj1._y)

obj1.public_method()
obj1._protected_method()

