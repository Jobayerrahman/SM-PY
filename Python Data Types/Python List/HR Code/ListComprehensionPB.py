List = []

x = int(input())
y = int(input())
z = int(input())
n = int(input())

#Normal nasted loop
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n and i+j+k <n:
                List.append([i,j,k])

print("With Nasted Loop : ")
print(List)

#List Comprehension
listcomp = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
print("With List Comprehension :")
print(listcomp)
