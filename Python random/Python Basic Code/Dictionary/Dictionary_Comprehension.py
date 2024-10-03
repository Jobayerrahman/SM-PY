#Dictionary Comprehension: Given a list of integers, write a Python program to create a dictionary where the keys are the elements from the list, and the values are their squares.

List = [4,5,6,7,8,9,10]
Dict = {}

# for i in range(len(List)):
#     Dict[i] = List[i]*List[i]

Dict = {i: List[i]*List[i] for i in range(len(List)) }

print(Dict)
