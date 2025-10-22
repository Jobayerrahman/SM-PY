# Python Class Constructor Example

class MyFirstClass:
    # Class variables (shared by all objects)
    x = 100
    y = 200
    z = 300

    # Constructor method
    def __init__(self):
        # Runs automatically when the object is created
        self.total = self.x + self.y + self.z
        print("Constructor called! Total calculated.")

# Creating an object
first_object = MyFirstClass()

# Accessing class variables using the object
print("Value of x:", first_object.x)
print("Value of y:", first_object.y)
print("Value of z:", first_object.z)

# Accessing the variable created inside the constructor
print("Summation of x + y + z:", first_object.total)

# Printing the object
print(first_object)   # Shows object memory address


