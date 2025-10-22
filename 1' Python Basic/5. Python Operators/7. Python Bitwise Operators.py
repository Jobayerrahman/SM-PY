'''
 7. Python Bitwise Operators
    What are Bitwise Operators?
    - Bitwise operators work on **bits** (0s and 1s) at the binary level.
    - They are used to perform bit-level operations on integers.

| Operator | Name              | Description                                                                 | Example (a=10, b=4) | Result |
| -------- | ----------------- | --------------------------------------------------------------------------- | ------------------- | ------- |
| &        | Bitwise AND       | Returns 1 if both bits are 1                                                | a & b              | 0       |
| |        | Bitwise OR        | Returns 1 if at least one bit is 1                                          | a | b              | 14      |
| ^        | Bitwise XOR       | Returns 1 if bits are different                                             | a ^ b              | 14      |
| ~        | Bitwise NOT       | Inverts all bits (changes 1→0 and 0→1), result = -(a+1)                     | ~a                 | -11     |
| <<       | Left Shift        | Shifts bits to the left, adds 0s from the right (equivalent to a * 2ⁿ)      | a << 2             | 40      |
| >>       | Right Shift       | Shifts bits to the right, removes bits from the right (equivalent to a // 2ⁿ) | a >> 2           | 2       |

Note: Bitwise operations only work with integers, because they use binary representation.
'''

# Example values
a = 10   # Binary: 1010
b = 4    # Binary: 0100

print("a =", a, "→ Binary:", bin(a))
print("b =", b, "→ Binary:", bin(b))
print()

# Bitwise AND
print("a & b =", a & b)   # 1010 & 0100 = 0000 (0)

# Bitwise OR
print("a | b =", a | b)   # 1010 | 0100 = 1110 (14)

# Bitwise XOR
print("a ^ b =", a ^ b)   # 1010 ^ 0100 = 1110 (14)

# Bitwise NOT
print("~a =", ~a)         # Inverts bits of 1010 → ...11110101 → -11

# Left Shift
print("a << 2 =", a << 2) # 1010 << 2 = 101000 (40)

# Right Shift
print("a >> 2 =", a >> 2) # 1010 >> 2 = 10 (2)
