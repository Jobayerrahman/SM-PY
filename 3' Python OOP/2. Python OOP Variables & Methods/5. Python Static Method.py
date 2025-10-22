'''
✅ What is a Static Method?

- A static method is a method that does not access instance variables or class variables.

    -- It belongs to the class, but it doesn’t require self or cls.

    -- It is defined using the '@staticmethod' decorator.

    -- It is used for utility functions that don’t need object or class data.

'''


class MathOperations:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


# Calling static methods using the class name
print(MathOperations.add(10, 20))       # 30
print(MathOperations.multiply(5, 4))    # 20


# ---------------------- Real-Life Example ----------------------


class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9


# Calling static methods directly using the class
print(TemperatureConverter.celsius_to_fahrenheit(37))   # 98.6
print(TemperatureConverter.fahrenheit_to_celsius(98.6)) # 37.0
