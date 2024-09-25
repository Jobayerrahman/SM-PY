#List Manipulation: Given two lists of integers, write a Python program to create a new list that contains elements common to both lists.
firstList = []
secondList = []

firstElNumber = int(input('Enter the number of elements for firstList : '))
for i in range(firstElNumber):
    elements = int(input('Enter the elements : '))
    firstList.append(elements)

print(end='')

secondElNumber = int(input('Enter the number of elements for secondList : '))
for i in range(secondElNumber):
    elements = int(input('Enter the elements : '))
    secondList.append(elements)


resultList = []
for i in range(0,len(firstList)):
    for j in range(0,len(secondList)):
        if firstList[i] == secondList[j]:
            resultList.append(firstList[i])

print(firstList)
print(secondList)
print(resultList)