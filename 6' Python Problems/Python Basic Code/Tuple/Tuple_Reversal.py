#Tuple Reversal: Write a Python program to reverse a tuple without using any
Tuple = (2,34,24,63,12,23,45,61)
List = list(Tuple)

ReversalList = []
for i in range(len(List)-1,-1,-1):
    ReversalList.append(List[i])

print(ReversalList)
