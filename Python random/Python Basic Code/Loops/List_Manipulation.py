#List Manipulation: Given a list of integers, write a Python program using a for loop to find the sum, average, maximum, and minimum values in the list.

List = []
number = int(input("Enter the number of element : "))

for i in range(0,number):
    element = int(input("Enter the element : "))
    List.append(element)

print(List)

Sum = 0
Max = 0
Min = float('inf')
for i in range(len(List)):
    Sum = Sum + List[i]
    if Max < List[i]:
        Max = List[i]
    if Min > List[i]:
        Min = List[i]



print('Sum of list element : ', Sum)
print('Average of list element : ',Sum/len(List))
print('Maximum element of list : ',Max)
print('Manimum element of list : ',Min)