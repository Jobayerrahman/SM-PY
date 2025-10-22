# The print() function is used to display output
variable_example = "This is a testing variable"
print(variable_example)


# ---------------------- ****************** ----------------------|


# We can print multiple variables separated by commas
a = "Apple"
b = "Banana"
c = "Cherry"

print(a, b, c)


# ---------------------- ****************** ----------------------|

# The + operator adds numbers and concatenates strings
number1 = 10
number2 = 50

string1 = "Your "
string2 = "Name"
string3 = "?"

print("Sum of number1 and number2:", number1 + number2)
print("Concatenation of strings:", string1 + string2 + string3)


# ---------------------- ****************** ----------------------|


# If we try to combine a string and a number using +, Python gives an error
# print(number1 + a)  # ❌ TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ✅ Correct way: Use a comma or convert number to string
print(number1, a)
# OR
print(str(number1) + " " + a)
