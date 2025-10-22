#Type Conversion: Given a list of integers, write a Python program to convert each element of the list to a string.
#Two way to type conversion

#Using Map() Function
intList = [12, 34, 53, 11, 23]
stringList = map(str,intList)
resultList  = list(stringList)
print(resultList)


#Using for loop
outputList = []
for i in range(len(intList)):
    outputList.append(str(intList[i]))

print(outputList)