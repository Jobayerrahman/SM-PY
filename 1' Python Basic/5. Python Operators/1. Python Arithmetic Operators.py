'''
1. Python Arithmetic Operators
    - Python provides several arithmetic operators to perform mathematical calculations between numbers.

| Operator | Description                               | Example      |
| -------- | ----------------------------------------- | ------------ |
| `+`      | Addition                                  | 10 + 5 → 15  |
| `-`      | Subtraction                               | 10 - 5 → 5   |
| `*`      | Multiplication                            | 10 * 5 → 50  |
| `/`      | Division (returns float)                  | 10 / 5 → 2.0 |
| `%`      | Modulus (remainder)                       | 10 % 3 → 1   |
| `**`     | Exponentiation (power)                    | 2 ** 3 → 8   |
| `//`     | Floor Division (quotient without decimal) | 10 // 3 → 3  |

'''








# Python Arithmetic Operators

number01 = int(input("Enter the 1st number: "))
number02 = int(input("Enter the 2nd number: "))

# Addition
result01 = number01 + number02
print(f"Addition (+): {number01} + {number02} = {result01}")

# Subtraction
result02 = number01 - number02
print(f"Subtraction (-): {number01} - {number02} = {result02}")

# Multiplication
result03 = number01 * number02
print(f"Multiplication (*): {number01} * {number02} = {result03}")

# Division
result04 = number01 / number02
print(f"Division (/): {number01} / {number02} = {result04}")

# Modulus (Remainder)
result05 = number01 % number02
print(f"Modulus (%): {number01} % {number02} = {result05}")

# Exponentiation (Power)
result06 = number01 ** number02
print(f"Exponentiation (**): {number01} ** {number02} = {result06}")

# Floor Division (Integer Division)
result07 = number01 // number02
print(f"Floor Division (//): {number01} // {number02} = {result07}")
