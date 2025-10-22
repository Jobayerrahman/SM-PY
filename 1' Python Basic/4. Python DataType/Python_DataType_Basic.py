# Python has many built-in data types. Variables can store different types of data.
# Let's learn them with real-life product examples from an online shop.

# ---------------------- Text Type ----------------------
product_name = "Men's Navy Blue Jeans"  # string
print(type(product_name), product_name)


# ---------------------- Numeric Types ----------------------
product_stock = 25                     # int → whole number
product_price = 299.99                 # float → decimal number
discount_rate = 0.10                   # float → 10% discount

# Complex numbers are used rarely in real projects, except in AI/ML and signal processing
complex_data_01 = 3 + 4j
complex_data_02 = complex(1, -2)
product_complex_data = complex_data_01 * complex_data_02

print(type(product_stock), product_stock)
print(type(product_price), product_price)
print(type(product_complex_data), product_complex_data)


# ---------------------- Sequence Types ----------------------
product_colors = ["Red", "White", "Black"]          # list → ordered & changeable
available_sizes = ("M", "L", "XL", "XXL")           # tuple → ordered but not changeable
top_selling_products = range(1, 11)                 # range → sequence of numbers

print(type(product_colors), product_colors)
print(type(available_sizes), available_sizes)
print(type(top_selling_products), list(top_selling_products))


# ---------------------- Mapping Type ----------------------
product = {
    "name": "Men's Navy Blue Jeans",
    "price": 299.99,
    "stock": 25
}  # dictionary → key-value pairs

print(type(product), product)


# ---------------------- Set Types ----------------------
unique_colors = {"Red", "White", "Black"}           # set → unordered, no duplicates
unique_sizes = frozenset({"M", "L", "XL"})          # frozenset → unchangeable set

print(type(unique_colors), unique_colors)
print(type(unique_sizes), unique_sizes)


# ---------------------- Boolean Type ----------------------
in_stock = True     # bool → True or False
free_shipping = False

print(type(in_stock), in_stock)


# ---------------------- Binary Types ----------------------
# Rare in beginner-level but used in images, files, and network data.
product_bytes = b"Jeans"                    # bytes → immutable binary data
product_byte_array = bytearray(5)           # bytearray → mutable binary data
product_memory_view = memoryview(bytes(5))  # memoryview → efficient binary view

print(type(product_bytes), product_bytes)


# ---------------------- None Type ----------------------
product_discount = None  # None means 'no value' or 'empty'
print(type(product_discount), product_discount)
