#List Average: Write a Python program to calculate the average of all elements in a given list of integers.

List = []
elNumber = int(input('Enter the element of number : '))

for i in range(0,elNumber):
    element = int(input('Enter the elements : '))
    List.append(element)

Sum = 0
for i in range(len(List)):
    Sum = Sum + List[i]

Average = Sum / len(List)
print(Average)