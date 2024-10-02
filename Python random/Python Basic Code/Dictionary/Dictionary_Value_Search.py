#Dictionary Value Search: Given a dictionary of items and their prices, write a Python program to search for an item based on its price and print the item’s name.
# dict = {}

# num_entries = int(input('Enter the number of entries you want to add: '))

# for i in range(num_entries):
#     key = input('Enter the Key name : ')
#     value = input('Enter the value : ')
#     dict[key] = value

fruit = {'apple' : 1, 'mango' : 2, 'cherry' : 3}

price = 20
res =''
for key in fruit:
    if dict[key] == price:
        res = key

print(res)