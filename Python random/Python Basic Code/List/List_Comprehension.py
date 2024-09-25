#List Comprehension: Given a list of integers, write a Python program to create a new list that contains the squares of the elements using list comprehension.
List = []
elNumber = int(input('Enter the number of element : '))

for i in range(elNumber):
    elements = int(input('Enter the element : '))
    List.append(elements)

resultList = [List[i]**2 for i in range(len(List))]

print(resultList)