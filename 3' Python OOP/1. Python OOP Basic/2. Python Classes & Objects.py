# Class definition
class MyFirstClass:
    # Class variables (shared by all objects created from this class)
    x = 100
    y = 200
    z = 300

    # Method to calculate the summation of x, y, and z
    def summation_method(self):
        print("Summation of x + y + z:", self.x + self.y + self.z)


# Creating an object (instance) of the class
first_object = MyFirstClass()

# Accessing class variables using the object
print("Accessing class variable x:", first_object.x)
print("Accessing class variable y:", first_object.y)
print("Accessing class variable z:", first_object.z)

# Calling a class method
first_object.summation_method()



