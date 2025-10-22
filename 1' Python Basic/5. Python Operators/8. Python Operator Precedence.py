'''
6. Python Operator Precedence
    - Operator precedence determines the order in which operations are performed in an expression.
    - When multiple operators appear in the same expression, Python evaluates them according to precedence (priority).
    - For example, * and / have higher precedence than + and -.

| Precedence | Operator(s)                      | Description                                            |
| ----------- | -------------------------------- | ------------------------------------------------------ |
| 1           | ()                               | Parentheses (used to override precedence)              |
| 2           | **                               | Exponentiation                                         |
| 3           | +x, -x, ~x                       | Unary plus, minus, bitwise NOT                         |
| 4           | *, /, //, %                      | Multiplication, division, floor division, modulus      |
| 5           | +, -                             | Addition and subtraction                               |
| 6           | <<, >>                           | Bitwise shift operators                                |
| 7           | &                                | Bitwise AND                                            |
| 8           | ^                                | Bitwise XOR                                            |
| 9           | |                                | Bitwise OR                                             |
| 10          | <, <=, >, >=, ==, !=             | Comparison operators                                   |
| 11          | not                              | Logical NOT                                            |
| 12          | and                              | Logical AND                                            |
| 13          | or                               | Logical OR                                             |
| 14          | =, +=, -=, *=, /=, //=, %=, **=  | Assignment and augmented assignment                    |
'''

# Example 1: Basic Precedence
result = 10 + 5 * 2
print(result)   # Output: 20
# Explanation: * has higher precedence than +


# Example 2: Using Parentheses
result = (10 + 5) * 2
print(result)   # Output: 30
# Explanation: Parentheses override normal precedence


# Example 3: Exponentiation and Multiplication
result = 2 + 3 ** 2 * 2
print(result)   # Output: 20
# Steps: 3 ** 2 = 9, then 9 * 2 = 18, finally 2 + 18 = 20


# Example 4: Logical Precedence
x = 5
print(x > 3 and x < 10)         # True
print(not (x > 3 and x < 10))   # False
# Explanation: Comparison -> and -> not


# Example 5: Combining Multiple Operators
result = 5 + 2 * 3 ** 2
print(result)   # Output: 23
# Steps: 3 ** 2 = 9, 2 * 9 = 18, 5 + 18 = 23
