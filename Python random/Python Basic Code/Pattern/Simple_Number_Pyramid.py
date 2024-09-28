#Simple Number Pyramid

rows = int(input('Enter the number of rows : '))

for number in range(rows+1):
    for j in range(number):
        print(number,end='')
    
    print()

