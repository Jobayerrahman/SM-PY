"""
✅ What is a Constructor in Python?

- A constructor is a special method in a class.
- In Python, the constructor method is __init__.
- It is called automatically when an object is created.
- It is used to initialize (assign) values to object properties.
- It is a special type of instance method.
"""

class Person:
    # Constructor method
    def __init__(self, name, age):
        # Instance variables (unique for each object)
        self.name = name
        self.age = age
        print(f"✅ A new Person object is created for {self.name}")

# Creating objects from the class (Instances)
p1 = Person("John", 45)
p2 = Person("Alice", 30)

# Accessing object properties
print("Person 1 Name:", p1.name)
print("Person 1 Age:", p1.age)

print("Person 2 Name:", p2.name)
print("Person 2 Age:", p2.age)

