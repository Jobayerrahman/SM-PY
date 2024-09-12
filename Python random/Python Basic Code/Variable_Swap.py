#Write a Python program to swap the values of two variables without using a temporary variable.
variable_one = 10
variable_two = 24

print("Variable_One: ", variable_one)
print("Variable_Two: ", variable_two)

variable_one = variable_one + variable_two
variable_two = variable_one - variable_two
variable_one = variable_one - variable_two

print("Variable_One: ", variable_one)
print("Variable_Two: ", variable_two)