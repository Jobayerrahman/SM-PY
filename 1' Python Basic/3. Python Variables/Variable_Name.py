# ✅ Variable Naming Examples in Python

# A variable can have a short name or a descriptive name
x = 3
y = 5
age = 30  # Variable names are case-sensitive
Age = 40  # "Age" is different than "age" and "AGE" (case-sensitive)
AGE = 50  # "AGE" is also different from "Age" and "age"
car_name = "BMW"
total_cost = 500.99

# ---------------------- Valid Variable Names ----------------------

myvar = "Valid variable name"  # Starts with a letter
myvar2 = "Valid variable name"  # Contains numbers after letter
_my_var = "Valid variable name"  # Can start with underscore

print(myvar)
print(myvar2)
print(_my_var)

# ---------------------- Variable Name Styles ----------------------

my_variable_name = "Snake Case"  # snake_case
myVariableName = "Camel Case"  # camelCase
MyVariableName = "Pascal Case"  # PascalCase

print(my_variable_name)
print(myVariableName)
print(MyVariableName)

# ---------------------- Constants (by convention) ----------------------

MYVAR = "This is a constant (by naming convention)"
print(MYVAR)

# ---------------------- Invalid Variable Names ----------------------

# 2myvar = "Invalid - starts with number"
# my-var = "Invalid - hyphens not allowed"
# my var = "Invalid - spaces not allowed"
# for = "Invalid - Python keyword"
