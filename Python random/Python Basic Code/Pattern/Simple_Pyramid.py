# Simple Python program to print the Simple pyramid pattern   

rowNumber =  int(input('Enter the row number : '))

for i in range(rowNumber):
    for j in range(0, i+1):
        print("*",end='')
    print()