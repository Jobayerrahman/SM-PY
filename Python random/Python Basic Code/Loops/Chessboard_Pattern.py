#Chessboard Pattern: Write a Python program using nested loops to print a chessboard pattern (alternating “X” and “O” characters) of size 8×8.34. 
#Number Pyramid: Write a Python program using nested loops to print a number pyramid like the following: 1 22 333 4444 55555

rows  = int(input('Enter the row number : '))

for number in range(rows+1):
    for i in range(number):
        print(number,end='')

    print()