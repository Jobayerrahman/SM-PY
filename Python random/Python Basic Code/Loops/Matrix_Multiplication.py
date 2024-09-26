#Matrix Multiplication: Write a Python program using nested loops to multiply two matrices. 3x3 matrix

List01 = [[1,2,3],[2,3,4],[3,4,5]]
List02 = [[1,2,3],[2,3,4],[3,4,5]]
result01 = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(List01)):
    for j in range(len(List01[i])):
        result01[i][j] = List01[i][j] * List02[i][j]

for r in result01:
    print(r)


#Matrix Multiplication: Write a Python program using nested loops to multiply two matrices. 3x3 matrix and 3x4 matrix
List03 = [[1,2,3],[2,3,4],[3,4,5]]
List04 = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
result02 = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(len(List03)):
    for j in range(len(List04[i])):
        for k in range(len(List04)):
            result02[i][j] = List03[i][k] * List04[k][j]

for r in result02:
    print(r)
