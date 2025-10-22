
'''
4. Python Logical Operators
    - Logical operators are used to combine multiple conditions and control the program’s flow based on whether conditions are True or False.

| Operator | Description                                     | Example             | Result                        |
| -------- | ----------------------------------------------- | ------------------- | ----------------------------- |
| `and`    | Returns `True` if **both** conditions are true  | `(a > 0 and b > 0)` | True if both positive         |
| `or`     | Returns `True` if **any one** condition is true | `(a > 0 or b > 0)`  | True if at least one positive |
| `not`    | Reverses the logical result                     | `not(a > 0)`        | True if `a > 0` is False      |

'''


# Python Logical Operators

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("\nLogical Operator Results:\n")

# and operator → Both conditions must be True
print("a > 0 and b > 0 →", a > 0 and b > 0)

# or operator → At least one condition must be True
print("a > 0 or b > 0 →", a > 0 or b > 0)

# not operator → Reverses the condition result
print("not(a > 0) →", not(a > 0))


# ---------------------- Real-life Example: Validation Checking ----------------------


age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ")

if age >= 18 and has_ticket.lower() == "yes":
    print("✅ You can enter the event.")
else:
    print("❌ Entry denied.")
