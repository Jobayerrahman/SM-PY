#Duplicate Removal: Write a Python program that takes a list of elements as input and creates a new set containing only the unique elements from the list.
elNaumer = int(input('Enter the number of element : '))
List = []

for i in range(elNaumer):
    element = int(input('Enter the element : '))
    List.append(element)


print(set(List))
