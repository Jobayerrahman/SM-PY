'''✅ What is a Class Method?

- A class method is a method that belongs to the class, not to a specific object.

    -- It uses the @classmethod decorator.

    -- It takes cls as the first parameter instead of self.

    -- It can access and modify class variables, but cannot access instance variables.

    -- Class methods are often used as factory methods—methods that return class objects in different ways.'''


# ---------------------- Example 01 ----------------------


class Student:
    school_name = "Greenwood High"  # Class variable

    def __init__(self, name, grade):
        self.name = name  # Instance variable
        self.grade = grade

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name  # Modifying class variable


# Using class method without creating an object
Student.change_school("Sunrise Public School")
print(Student.school_name)


# ---------------------- Example 02 ----------------------


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split("-")
        return cls(name, int(salary))  # Using constructor to create object


# Creating object normally
emp1 = Employee("John", 50000)

# Creating object using class method
emp2 = Employee.from_string("Alice-60000")

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)
