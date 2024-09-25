#List Duplicates Removal: Write a Python program to remove duplicates from a given list while preserving the order of the elements.
List = []
elNumber = int(input('Enter the number of element : '))

for i in range(elNumber):
    elements = int(input('Enter the element : '))
    List.append(elements)

uniqueList = []
for i in range(0,len(List)):
    if List[i] not in uniqueList:
        uniqueList.append(List[i])

print(uniqueList)