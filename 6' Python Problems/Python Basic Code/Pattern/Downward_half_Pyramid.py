# Simple Python program to print the simple downward half - pyramid pattern    
rowNumber =  int(input('Enter the row number : '))

for i in range(rowNumber+1,0,-1):
    for j in range(0,i-1):
        print('^',end='')
    print()