Object-oriented programming
---------------------------
1. &nbsp; [OOP](https://github.com/Yuki69Okita/MyOOPPythonJorney#1-oop) <br />
2. &nbsp; [Process:](https://github.com/Yuki69Okita/MyOOPPythonJorney#2-process) <br />
   1. &nbsp; [Class](https://github.com/Yuki69Okita/MyOOPPythonJorney#class) <br />
   2. &nbsp; [Object](https://github.com/Yuki69Okita/MyOOPPythonJorney#object) <br />
3. &nbsp; [Types of Attributes:](https://github.com/Yuki69Okita/MyOOPPythonJorney#3-types-of-attributes) <br />
   1. &nbsp; [Instance Attribute](https://github.com/Yuki69Okita/MyOOPPythonJorney#instance-attribute) <br />
   2. &nbsp; [Class Attribute](https://github.com/Yuki69Okita/MyOOPPythonJorney#class-attribute) <br />
4. &nbsp; [Types of Methods:](https://github.com/Yuki69Okita/MyOOPPythonJorney#4-types-of-methods) <br />
   1. &nbsp; [Instance Method](https://github.com/Yuki69Okita/MyOOPPythonJorney#instance-method) <br />
   2. &nbsp; [Class Method](https://github.com/Yuki69Okita/MyOOPPythonJorney#class-method) <br />
   3. &nbsp; [Static Method](https://github.com/Yuki69Okita/MyOOPPythonJorney#static-method) <br />
5. &nbsp; [Decorators:](https://github.com/Yuki69Okita/MyOOPPythonJorney#5-decorators)<br />
   1. &nbsp; [Built-in Decorator](https://github.com/Yuki69Okita/MyOOPPythonJorney#built-in-decorator)<br />
   2. &nbsp; [User-defined Decorator](https://github.com/Yuki69Okita/MyOOPPythonJorney#user-defined-decorator)<br />
6. Main Concepts:<br />
   1. &nbsp; [Inheritance](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Inheritance#inheritance)<br />
      1. &nbsp; [Single Inheritance](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Inheritance#1-single-inheritance)<br />
      2. &nbsp; [Multiple Inheritance](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Inheritance#2-multiple-inheritances)<br />
      3. &nbsp; [Multilevel Inheritance](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Inheritance#3-multilevel-inheritance)<br />
      4. &nbsp; [Hierarchical Inheritance](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Inheritance#4-hierarchical-inheritance)<br />
      5. &nbsp; [Hybrid Inheritance](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Inheritance#5-hybrid-inheritance)<br />
   2. &nbsp; [Polymorphism](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Polymorphism#polymorphism)<br />
      1. &nbsp; [Built-in Polymorphism](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Polymorphism#1-built-in-polymorphism)<br />
      2. &nbsp; [User-defined Function Polymorphism](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Polymorphism#2-user-defined-function-polymorphism)<br />
      3. &nbsp; [Polymorphism with Class](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Polymorphism#3-polymorphism-with-class)<br />
      4. &nbsp; [Polymorphism with Class Inheritance](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Polymorphism#4-polymorphism-with-class-inheritance)<br />
      5. &nbsp; [Polymorphism with Class and Function](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Polymorphism#5-polymorphism-with-class-and-function)<br />
   3. &nbsp; [Abstract](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Abstract#abstract)<br />
   4. &nbsp; [Encapsulation](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Encapsulation#encapsulation)<br />
      1. &nbsp; [Protected Members](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Encapsulation#1-protected-members)<br />
      2. &nbsp; [Private Members](https://github.com/Yuki69Okita/MyOOPPythonJorney/tree/main/Encapsulation#2-private-members)<br />

-----------------------
## 1. OOP:

- A way of structuring a program by grouping related properties and behaviors into separate objects
------------------
## 2. Process:

### Class
- Contains a blueprint or prototype (attributes and methods) from which objects are created

#### Example:
```python
class Dog:
    breed = "French Bulldog"

    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Bark! Bark!")
```
- Explanation:
  - There is a class with name "Dog"
  - In this class there is class attribute ("breed")
  - \_\_init__ 
    - function that makes attributes independent of each object
  - self
    - keyword for reference to the current instance of the class and is used to access variables that belong to the class
  - And instance method bark
    - which is printing a string

--------------------
### Object
- An entity that has a state and behavior associated with it

#### Example:
```python
dog1 = Dog("Lizzy")

print(f"Dog name: {dog1.name}, Dog breed: {dog1.breed}")
dog1.bark()
```
- Explanation:
  - After created class we need to create object from this class
  - dog1 is an object from it with name "Lizzy"
  - print() 
    - to print attributes dog1 have
  -  We call the .bark() method

#### Result:
![class-process.png](Images/class-process.png)

--------------------
## 3. Types of Attributes:
### Instance Attribute
- For each instance it can be a different attribute value

#### Example:
```python
class Dog:
    def __init__(self, breed):
        self.breed = breed


dog1 = Dog("French Bulldog")
print(dog1.breed)

dog2 = Dog("Huski")
print(dog2.breed)

dog3 = Dog("Huski")
dog3.breed = "Mops"
print(dog3.breed)
```
- Explanation:
  - There are 3 objects with different breed
  - You can change the attribute like dog3

#### Result:
![instance-attribute.png](Images/instance-attribute.png)

----------------------------
### Class Attribute
- The value of the attribute applies to all instances in the class
#### Example:
```python
class Dog:
    breed = "French Bulldog"


dog1 = Dog()
print(dog1.breed)

dog2 = Dog()
print(dog2.breed)

Dog.breed = "Mops"
dog3 = Dog()
print(dog3.breed)
```
- Explanation:
  -  There are 2 objects with the same breed
  - You can change the breed attribute, but it will apply for all objects after the change

    
#### Result:<br />
![class-attribute.png](Images/class-attribute.png)

------------------
## 4. Types of Methods:

### Instance Method
- Is bound to the instance of the class 
  - Able to modify the state of the object
  - Able to access and modify the class itself and its variables

#### Example:
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def edit_name(self, edited_name):
        self.name = edited_name


dog1 = Dog("Pepe")
dog2 = Dog("Lily")
print(f"Before edit: {dog1.name} and {dog2.name}")

Dog.edit_name(dog2, "Lilly")
print(f"After edit: {dog1.name} and {dog2.name}")
```
- Explanation:
  - Here we are replacing the old name with new one

#### Result:
![instance-method.png](Images/instance-method.png)

----------------------
### Class Method
- Is bound to the class 
  - Able to modify the state of the class
  - Able to access the variables of the class itself

#### Example:
```python
import datetime


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my dog name is {self.name} and he is {self.age} years old.")

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = datetime.datetime.now().year - birth_year
        return cls(name, age)


dog1 = Dog("Pepe", 5)
dog1.greet()

dog2 = Dog.from_birth_year("Bob", 2021)
dog2.greet()
```
- Explanation:
  - This class can create objects with name and age
  - After created object we can call .greet method
    - Where it's printing string with respective names and years
  - @classmethod
    - decorator for defining a class method
  - cls
    - keyword for class reference
  - from_birth_year()
    - we are calculating what age is if the argument is a year
      - that is why datetime is imported
    - it's returning all needed data

#### Result:
![class-method.png](Images/class-method.png)

-----------------------
### Static Method
- Is bound to the class 
  - Not able to modify the state of the class or object
  - Not able to access or modify the class itself and its instance variables

#### Example:
```python
class Dog:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def spelling(name):
        list_words = []
        for word in name:
            list_words.append(word)

        return list_words


dog1 = Dog("Pepe")
print(dog1.spelling(dog1.name))
```
- Explanation:
  - Just like normal function but in class like method

#### Result:
![static-method.png](Images/static-method.png)

-------------------------
## 5. Decorators:
- A way to modify the behavior of a class or function without changing its source code

### Built-in Decorator
- There are different decorators for different reasons like @staticmethod, @classmethod and so on

#### Example:
```python
class Dog:
    @staticmethod
    def speak():
        return "Bark! Bark!"

    
dog1 = Dog()
print(dog1.speak())
```
- Explanation:
  - They are easy to use and more readable code

#### Result:
![built-in-decorator.png](Images/built-in-decorator.png)

---------------------
### User-defined Decorator
- Functions that take another function as an argument and then return the modified function

#### Example:
```python
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper


@my_decorator
def say_hello():
    print("Hello World!")


say_hello()
```
- Explanation:
  - my_decorator - takes a function as input and returns another function
  
#### Result:
![ud-decorator.png](Images/ud-decorator.png)
