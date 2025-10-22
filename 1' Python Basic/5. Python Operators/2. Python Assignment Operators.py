'''
2. Python Assignment Operators
    - Assignment operators are used to assign values to variables and can also perform operations while assigning.

| Operator | Example   | Equivalent To | Description                |
| -------- | --------- | ------------- | -------------------------- |
| `=`      | `x = 5`   | —             | Assigns value 5 to `x`     |
| `+=`     | `x += 3`  | `x = x + 3`   | Adds and assigns           |
| `-=`     | `x -= 3`  | `x = x - 3`   | Subtracts and assigns      |
| `*=`     | `x *= 3`  | `x = x * 3`   | Multiplies and assigns     |
| `/=`     | `x /= 3`  | `x = x / 3`   | Divides and assigns        |
| `%=`     | `x %= 3`  | `x = x % 3`   | Modulus and assigns        |
| `**=`    | `x **= 3` | `x = x ** 3`  | Exponentiation and assigns |
| `//=`    | `x //= 3` | `x = x // 3`  | Floor division and assigns |

'''



# Python Assignment Operators

x = int(input("Enter a number: "))

print("\nInitial value of x:", x)

x += 5
print("After x += 5 →", x)  # Adds 5

x -= 3
print("After x -= 3 →", x)  # Subtracts 3

x *= 2
print("After x *= 2 →", x)  # Multiplies by 2

x /= 4
print("After x /= 4 →", x)  # Divides by 4 (returns float)

x %= 3
print("After x %= 3 →", x)  # Remainder of division by 3

x = 5
x **= 3
print("After x **= 3 →", x)  # Raises to the power of 3

x = 10
x //= 3
print("After x //= 3 →", x)  # Floor division (integer result)
