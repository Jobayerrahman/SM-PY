#Dictionary Length: Write a Python program to calculate and print the number of key-value pairs in a given dictionary.
dict = {}

num_entries = int(input('Enter the number of entries you want to add: '))

for i in range(num_entries):
    key = input('Enter the Key name : ')
    value = input('Enter the value : ')
    dict[key] = value

print(len(dict.keys()))
print(len(dict.values()))