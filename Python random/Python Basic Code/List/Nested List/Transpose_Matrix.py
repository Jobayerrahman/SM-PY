#Transpose Matrix: Write a Python program to transpose a given matrix represented as a nested list.

List = [[1,2],[2,3],[3,4]]
result = [[0,0,0],[0,0,0]]

for i in range(len(List)):
    for j in range(len(List[0])):
        result[j][i] = List[i][j]

for r in result:
    print(r)