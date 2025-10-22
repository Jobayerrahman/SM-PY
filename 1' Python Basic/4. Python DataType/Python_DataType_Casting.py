# Type conversion (type casting) means changing one data type to another

x = str(3)     # Convert integer 3 to string "3"
y = int(3)     # Keep 3 as an integer
z = float(3)   # Convert integer 3 to float 3.0

print(x)       # Output: "3" (string)
print(y)       # Output: 3 (integer)
print(z)       # Output: 3.0 (float)

print(type(x))  # <class 'str'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'float'>




# ---------------------- Real-Life Example ----------------------

# Example: User enters age as text from an input form

user_age_text = "25"          # Text from user input
user_age_number = int(user_age_text)   # Convert to integer for calculation

next_year_age = user_age_number + 1

print("Next year you will be:", next_year_age)
