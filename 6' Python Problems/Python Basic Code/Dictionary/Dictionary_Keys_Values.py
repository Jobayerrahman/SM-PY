#Dictionary Keys and Values: Write a Python program that takes a dictionary as input and prints all the keys and values in separate lines.
dict = {}

num_entries = int(input('Enter the number of entries you want to add: '))

for i in range(num_entries):
    key = input('Enter the Key name : ')
    value = input('Enter the value : ')
    dict[key] = value


print('All keys : ',dict.keys())
print('All values : ',dict.values())