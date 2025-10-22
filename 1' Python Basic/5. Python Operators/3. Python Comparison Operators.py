'''
3. Python Comparison Operators
    -Comparison operators are used to compare two values.
    They always return a Boolean result — either True or False.

| Operator | Example  | Description                                           |
| -------- | -------- | ----------------------------------------------------- |
| `==`     | `x == y` | Returns `True` if both values are equal               |
| `!=`     | `x != y` | Returns `True` if values are not equal                |
| `>`      | `x > y`  | Returns `True` if `x` is greater than `y`             |
| `<`      | `x < y`  | Returns `True` if `x` is less than `y`                |
| `>=`     | `x >= y` | Returns `True` if `x` is greater than or equal to `y` |
| `<=`     | `x <= y` | Returns `True` if `x` is less than or equal to `y`    |

'''


# Python Comparison Operators

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("\nComparison Operator Results:\n")

print("a == b →", a == b)   # Equal to
print("a != b →", a != b)   # Not equal to
print("a > b  →", a > b)    # Greater than
print("a < b  →", a < b)    # Less than
print("a >= b →", a >= b)   # Greater than or equal to
print("a <= b →", a <= b)   # Less than or equal to



#Chaining Comparison Operators

x= 5
print(1< x < 10)
print(1 < x and x < 10)