"""
* What is OOP?
--> OOP stands for Object-Oriented Programming.
--> It is a way of structuring code using classes and objects.
"""

"""
* Why do we need OOP?
--> OOP helps organize complex programs.
--> It makes code reusable, modular, and easier to maintain.
--> It helps follow the DRY principle: Don't Repeat Yourself.
"""

"""
* Does Python support OOP?
--> Yes, Python is an Object-Oriented Programming language.
"""

"""
* Advantages of OOP:
--> Makes code reusable and modular.
--> Increases code readability and organization.
--> Helps in debugging and maintaining large projects.
--> Provides security through encapsulation.
--> Supports real-world modeling using classes and objects.
"""

"""
* What is a Class?
--> A class is a blueprint/template for creating objects.
--> It defines properties (variables) and behaviors (methods).
"""

"""
* What is an Object?
--> An object is an instance of a class.
--> When we create an object from a class, it can use the
   variables and functions defined inside that class.
--> Example: Class = Car, Objects = BMW, Audi, Toyota
"""


# Example Classes
class Fruit:
    def __init__(self, name): # __init__ runs automatically when object is created
        self.name = name # self.name belongs to the object


class Car:
    def __init__(self, brand): # __init__ runs automatically when object is created
        self.brand = brand # self.brand belongs to the object


# Creating objects from the Fruit class
apple = Fruit("Apple")
banana = Fruit("Banana")
cherry = Fruit("Cherry")

# Creating objects from the Car class
volvo = Car("Volvo")
audi = Car("Audi")
toyota = Car("Toyota")

# Printing object information
print("Fruit Objects:")
print(apple.name)
print(banana.name)
print(cherry.name)

print("\nCar Objects:")
print(volvo.brand)
print(audi.brand)
print(toyota.brand)
