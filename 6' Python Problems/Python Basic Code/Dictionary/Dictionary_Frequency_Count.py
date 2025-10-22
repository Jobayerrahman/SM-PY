#Dictionary Frequency Count: Write a Python program that takes a string as input and creates a dictionary containing each character as a key and its frequency as the value.

Dict = dict()
key = 0

string_input = input('Enter the string : ')

for s in string_input:
    Dict[key] = s
    key += 1

print(Dict)