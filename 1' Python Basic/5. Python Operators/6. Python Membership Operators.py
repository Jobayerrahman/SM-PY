'''
6. Python Membership Operators
-------------------------------
Membership operators are used to **check whether a value or variable exists** in a sequence 
(such as a string, list, tuple, set, or dictionary).

| Operator   | Description                                           | Example          | Result |
| ----------- | ----------------------------------------------------- | ---------------- | ------- |
| `in`        | Returns True if the value exists in the sequence      | `"apple" in x`   | True    |
| `not in`    | Returns True if the value does NOT exist in sequence  | `"apple" not in x` | False  |
'''


#Example 1: Using 'in' with a list
fruits = ["apple", "banana", "cherry"]

print("Fruits list:", fruits)
print("'banana' in fruits →", "banana" in fruits)   # True → found in list
print("'mango' in fruits →", "mango" in fruits)     # False → not found
print()


#Example 2: Using 'not in' with a list
print("'grape' not in fruits →", "grape" not in fruits)  # True
print("'apple' not in fruits →", "apple" not in fruits)  # False
print()


#Example 3: Using 'in' with a string
message = "Welcome to Python programming!"

print("Message:", message)
print("'Python' in message →", "Python" in message)       # True
print("'Java' in message →", "Java" in message)           # False
print()


#Example 4: Using 'in' with a tuple
colors = ("red", "green", "blue")
print("'green' in colors →", "green" in colors)   # True
print("'yellow' not in colors →", "yellow" not in colors)  # True
print()


#Example 5: Using 'in' with a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print("'name' in person →", "name" in person)   # True → checks keys, not values
print("'Alice' in person →", "Alice" in person) # False → only checks keys
print()


# ---------------------- Real-life Example ----------------------


username_list = ["admin", "manager", "user"]
user_input = input("Enter your username: ")

if user_input in username_list:
    print("✅ Access granted.")
else:
    print("❌ Access denied. Unknown username.")
