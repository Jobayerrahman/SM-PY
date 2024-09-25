#List Filtering: Given a list of integers, write a Python program to create a new list that contains only the even numbers from the original list.
 
elNumber = int(input('Enter the number of element : '))
List = []

for i in range(elNumber):
    elements = int(input('Enter the element value : '))
    List.append(elements)

filterList = []
for i in range(0,len(List)):
    if List[i] % 2 == 0:
        filterList.append(List[i])

print(filterList)