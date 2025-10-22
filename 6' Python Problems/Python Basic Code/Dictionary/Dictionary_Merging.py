#Dictionary Merging: Given two dictionaries, write a Python program to merge them into a single dictionary and print the result.


dict01 = {}
dict02 = {}
num_entries = int(input('Enter the number of entries you want to add: '))

for i in range(num_entries):
    key = input('Enter the Key name : ')
    value = input('Enter the value : ')
    dict01[key] = value

for i in range(num_entries):
    key = input('Enter the Key name : ')
    value = input('Enter the value : ')
    dict01[key] = value

result = dict01 | dict02
print(result)
