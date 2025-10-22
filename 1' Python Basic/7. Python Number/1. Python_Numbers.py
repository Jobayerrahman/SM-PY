"""
Python has three numeric types:
1. int     → Whole numbers, positive or negative (no decimals)
2. float   → Numbers with decimals (positive or negative)
3. complex → Complex numbers with a real and imaginary part (used in math, AI, or engineering)
"""

# Integer example
x = 1        # int
# Float example
y = 2.8      # float
# Complex example
z = 1j       # complex number, imaginary part is 1

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>


# ---------------------- Real-Life Example ----------------------


# Example: Store product details
product_stock = 50          # int
product_price = 129.99      # float
signal_strength = 2 + 3j    # complex number (for advanced electronics calculation)

print(product_stock, type(product_stock))
print(product_price, type(product_price))
print(signal_strength, type(signal_strength))
