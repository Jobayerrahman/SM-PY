#List Sum: Write a Python program to find the sum of all elements in a given list of integers.

List = []
elNumber = int(input("Enter the number of elements : "))

for i in range(0,elNumber):
    element = int(input("Enter the element value : "))
    List.append(element)

Sum = 0
for i in range(len(List)):
    Sum = Sum + List[i]

print(Sum)