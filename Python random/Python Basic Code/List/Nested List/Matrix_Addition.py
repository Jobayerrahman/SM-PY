#Matrix Addition: Write a Python program to add two matrices represented as nested lists.

List01 = [[1,3,4],[2,3,4],[1,2,4]]
List02 = [[1,3,4],[2,3,4],[1,2,4]]

resultList = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(List01)):
    for j in range(len(List01[i])):
        resultList[i][j] = List01[i][j] + List02[i][j]

for i in resultList:
    print(i)