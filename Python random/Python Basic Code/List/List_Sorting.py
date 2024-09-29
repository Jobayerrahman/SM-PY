#List Sorting: Write a Python program to sort a list of integers in ascending order.
List = []
elNumber = int(input('Enter the number of elements : '))

for i in range(0, elNumber):
    element = int(input("Enter the elements : "))
    List.append(element)


for i in range(0,len(List)):
    for j in range(i+1,len(List)):
        if List[i] > List[j]:
            temp = List[i]
            List[i] = List[j]
            List[j] = temp

print(List)
