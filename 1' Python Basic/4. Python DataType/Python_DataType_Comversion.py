# Type Conversion in Python (Casting)

x = 1        # int
y = 2.8      # float
z = 1j       # complex number

# Convert int to float
a = float(x)

# Convert float to int (decimal part removed)
b = int(y)

# Convert int to complex
c = complex(x)

print(a)  # 1.0
print(b)  # 2
print(c)  # (1+0j)

print(type(a))  # <class 'float'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'complex'>




# ---------------------- Real-Life Example ----------------------

# Example: Converting product price from string to number

price_text = "199.99"  # comes as string from user input or database
price_number = float(price_text)  # convert string to float

quantity = 3
total_price = quantity * price_number

print("Total Price:", total_price)  # 599.97
