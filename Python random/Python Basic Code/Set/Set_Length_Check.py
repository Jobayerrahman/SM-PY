#Set Length Check: Write a Python program that takes a set as input and prints the number of elements in the set.
# Set01 ={'Apple','Melon','Orange','Strawberry','Berry','Banana','Mango'}
# Set02 ={'Banana','Berry','Melon','Mango'}
List01 = []
List02 = []

elNumber = int(input('Enter the number of element : '))

for i in range(elNumber):
    elements = int(input('Enter the values : '))
    List01.append(elements)


for i in range(elNumber):
    elements = int(input('Enter the values : '))
    List02.append(elements)

Set01 = set(List01)
Set02 = set(List02)

print(len(Set01))
print(len(Set02))