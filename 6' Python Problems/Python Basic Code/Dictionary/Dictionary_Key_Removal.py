#Dictionary Key Removal: Given a dictionary of items and their quantities, write a Python program to remove a specific item from the dictionary based on user input.

player = {
    'name' : 'Zukar',
    'role' : 'jungler',
    'team' : 'Sk1',
    'kill' : 3,
    'fram' : 230,
    'ward' : 12,
    'death': 3
}

eliminate_key = str(input('Enter the key : '))
flag = False

for key in player.keys():
    if eliminate_key == key:
        flag = True
        break

if flag :
    del player[key]
else:
    print('Your given entry is not a key!')

print('Full dictionary after elimination : ',player)

