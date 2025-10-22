'''
✅ What are __str__ and __repr__?
    - Both __str__ and __repr__ are special methods in Python classes used to define string representations of objects.

        Methods:
            __str__	
                Purpose : User-friendly string, readable for end users	
                Used By : print(object)
            __repr__	
                Purpose : Official string, meant for developers, can be used to recreate object	
                Used By : repr(object) or in the console

        Rule of Thumb:
            __str__ → “nice to read”
            __repr__ → “official representation”
'''



class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # __str__ method (user-friendly)
    def __str__(self):
        return f"'{self.title}' by {self.author}, costs ${self.price}"

    # __repr__ method (official)
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price})"


# Create an object
book1 = Book("Python 101", "John Doe", 29.99)

# Using __str__ (user-friendly)
print(book1)  # Automatically calls __str__

# Using __repr__ (official / developer-friendly)
print(repr(book1))  # Calls __repr__

# Console interactive display
book1  # This will also call __repr__ by default
