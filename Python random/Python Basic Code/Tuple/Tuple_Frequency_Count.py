#Tuple Frequency Count: Given a tuple containing various elements, write a Python program to count the frequency of a specific element in the tuple.

Tuple = (2,1,4,5,6,1,3,5,5,3,5,4)
List01 = list(Tuple)
List02 = []
Dict = dict()

for i in List01:
    if i not in List02:
        List02.append(i)

for i in List02:
    Dict[i] = List01.count(i)

print(Dict)
    