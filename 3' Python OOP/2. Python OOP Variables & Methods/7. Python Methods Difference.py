'''
| Feature         | Constructor (__init__)         | Instance Method                     | Class Method                             | Static Method                               |
|-----------------|--------------------------------|-------------------------------------|------------------------------------------|---------------------------------------------|
| Decorator Used  | None                           | None                                | @classmethod                             | @staticmethod                                |
| First Parameter | self                           | self                                | cls                                      | No default parameter                         |
| Called When     | When object is created         | Any time using object               | Using class or object                    | Using class or object                        |
| Purpose         | Initialize object data         | Work with instance (object) data    | Work with class-level data               | General utility/helper functions             |
'''

class Example:
    class_variable = "I belong to the class"  # Class variable (shared by all objects)

    def __init__(self, value):  # Constructor
        self.value = value  # Instance variable (unique per object)

    def instance_method(self):  # Instance method
        return f"✅ Instance Method -> Instance value = {self.value}"

    @classmethod
    def class_method(cls):  # Class method
        return f"✅ Class Method -> Accessing class variable: {cls.class_variable}"

    @staticmethod
    def static_method():  # Static method
        return "✅ Static Method -> I don't use class or instance data"


# ----------- Using the class ----------- #

# Creating objects
obj1 = Example(10)
obj2 = Example(20)

# Calling instance method
print(obj1.instance_method())
print(obj2.instance_method())

# Calling class method
print(Example.class_method())
print(obj1.class_method())

# Calling static method
print(Example.static_method())
print(obj2.static_method())
