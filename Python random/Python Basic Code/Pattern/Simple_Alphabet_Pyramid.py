#Simple Alphabet Pyramid

rows = int(input('Enter the number of rows : '))
ascii_value = 65

for number in range(rows+1):
    for i in range(number+1):
        alphabet = chr(ascii_value)
        print(alphabet,end='')
    
    ascii_value += 1
    print()
