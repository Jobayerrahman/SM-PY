#Tuple Operations: Given two tuples of integers, write a Python program to perform element-wise addition, subtraction, and multiplication and create new tuples for each operation.
Tuple01 = (12,21,32,43,22,11)
Tuple02 = (2,3,4,5,6,7)
List01 = list(Tuple01)
List02 = list(Tuple02)

#Element-wise Addition
AdditionList = []
for i in range(0,len(Tuple01)):
    AdditionList.append(List01[i] + List02[i])

#Element-wise Subtraction
SubtractionList = []
for i in range(0,len(Tuple01)):
    SubtractionList.append(List01[i] - List02[i])

#Element-wise Multiplication
MultiplicationList = []
for i in range(0,len(Tuple01)):
    MultiplicationList.append(List01[i] * List02[i])

print("Main Tuple01 : ", Tuple01)
print("Main Tuple03 : ", Tuple01)
print("Addition Tuple : ",tuple(AdditionList))
print("Subtraction Tuple : ",tuple(SubtractionList))
print("Multiplication Tuple : ",tuple(MultiplicationList))

