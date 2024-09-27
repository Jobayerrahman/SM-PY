#Equilateral Pyramid of * Pattern

rows = int(input('Enter the number of rows : '))
m = (2*rows)-4
n = (2*rows)-4

print("Upward Pyramid : ",end='')
print()

for i in range(0,rows):
    for j in range(0,m):
        print(end=' ')
    
    m -=1
    for j in range(0,i+1):
        print('*',end=' ')
    
    print()


print("Downward Pyramid : ",end='')
print()

for i in range(rows+1,0,-1):
    for j in range(n,0,-1):
        print(end=' ')
    n +=1

    for j in range(0,i-1):
        print('*',end=' ')
    
    print()