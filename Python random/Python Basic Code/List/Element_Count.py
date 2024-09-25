#List Element Count: Write a Python program to count the occurrences of a specific element in a given list.

elNumber = int(input('Enter the number of element : '))
List = []
count = 0

for i in range(elNumber):
    elements = int(input('Enter the element : '))
    List.append(elements)

for i in range(0,len(List)):
    count +=1

print(count)
