#List Max and Min: Write a Python program to find the maximum and minimum values in a given list of integers.
List = []
elNumber = int(input('Enter the number of elements : '))

for i in range(0, elNumber):
    element = int(input("Enter the elements : "))
    List.append(element)

Max = 0
Min = float('inf')
for i in range(len(List)):
    if Max < List[i]:
        Max = List[i]
    if Min > List[i]:
        Min = List[i]
    
print("Max number is : ",Max)
print("Min number is : ",Min)