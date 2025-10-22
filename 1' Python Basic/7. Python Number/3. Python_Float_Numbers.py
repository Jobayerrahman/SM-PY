# Float (floating-point number) represents numbers with decimal points.
# These can be positive or negative and are commonly used for measurements, prices, percentages, etc.

x = 1.10        # simple decimal number
y = 234.5252    # float with multiple decimal places
z = -325.5522   # negative float number

print(type(x))  # <class 'float'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'float'>


# ---------------------- Real-Life Example ----------------------


# Example: Product pricing in an online shop
product_price = 1299.50
discount = 100.75
final_price = product_price - discount

print("Final Price:", final_price)
print(type(final_price))  # <class 'float'>
