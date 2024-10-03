#Dictionary Key Check: 
# Write a Python program that takes a key as input and checks if it exists in a given dictionary. 
# Print “Key Found” if the key is present and “Key Not Found” otherwise.

dict = {}
flag = False
num_entries = int(input('Enter the number of entries : '))

for i in range(num_entries):
    key = input('Enter the key : ')
    item = input('Enter the item : ')
    dict[key] = item

given_key = str(input('Enter the given key : '))

for key in dict.keys():
    if given_key == key:
        flag = True
        break

if flag:
    print('Key Found')
else:
    print('Key Not Found')