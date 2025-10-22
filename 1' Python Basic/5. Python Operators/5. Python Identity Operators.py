'''
5. Python Identity Operators
------------------------------
Identity operators are used to **compare the memory location** of two objects — not their values.
They check whether two variables actually **refer to the same object** in memory.

| Operator | Description                                                     | Example      | Result                            |
| -------- | --------------------------------------------------------------- | ------------ | --------------------------------- |
| `is`     | Returns True if both variables point to the same object         | `a is b`     | True if same memory location      |
| `is not` | Returns True if both variables point to different objects       | `a is not b` | True if different memory location |
'''

#Example 1: Python Identity Operators
a = ["apple", "banana"]
b = ["apple", "banana"]
c = a  # c points to the same memory location as a

print("a =", a)
print("b =", b)
print("c =", c)
print()

# 'is' operator → checks if both refer to the same memory object
print("a is b →", a is b)      # False → different memory locations
print("a is c →", a is c)      # True → same memory object
print()

# 'is not' operator → checks if both refer to different objects
print("a is not b →", a is not b)  # True → different memory
print("a is not c →", a is not c)  # False → same object
print()

#Checking object IDs to visualize memory differences
print("Memory ID of a:", id(a))
print("Memory ID of b:", id(b))
print("Memory ID of c:", id(c))
print()


#Example 2: Difference Between `is` and `==`
'''
🔹 `is`  → checks *identity* (same memory object)
🔹 `==`  → checks *equality* (same content/value)
'''

x = [1, 4, 5]
y = [1, 4, 5]

print("x == y →", x == y)   # True → values are the same
print("x is y →", x is y)   # False → different objects in memory
print()



#Example 3: Real-life use of `is` for None comparison
value = None
if value is None:
    print("✅ value is None (safe check using 'is')")
else:
    print("value is not None")
