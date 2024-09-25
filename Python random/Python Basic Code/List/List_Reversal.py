#List Reversal: Write a Python program to reverse a given list without using any built-in functions.

elNumber  = int(input('Enter the number of elements : '))
List = []
for i in range(elNumber):
    elements = int(input('Enter the element value : '))
    List.append(elements)

reverseList = []
count = len(List)

while count > 0:
    reverseList.append(List[count-1])
    count -= 1

print("Given List : ",List)
print("Reserve List : ",reverseList)
