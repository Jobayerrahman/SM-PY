#Tuple Sorting: Write a Python program to sort a tuple of integers in ascending order.

Tuple = (12,21,41,23,14,2)
List = list(Tuple)

for i in range(0,len(List)):
    for j in range(i+1,len(List)):
        if List[i] > List[j]:
            temp = List[i]
            List[i] = List[j]
            List[j] = temp
            
print(List) 