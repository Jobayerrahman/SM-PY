#Dictionary Value Search: Given a dictionary of items and their prices, write a Python program to search for an item based on its price and print the item’s name.
fruit = {'apple' : 20, 'mango' : 10, 'cherry' : 30}

def get_key(price):
    for key, value in fruit.items():
        if price == value:
            return key
    return "Key Doesn't Exist"

print(get_key(20))
print(get_key(10))