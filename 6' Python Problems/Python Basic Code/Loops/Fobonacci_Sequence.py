#Fibonacci Sequence: Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.
number = int(input("Enter the number : "))

number1 = 0
number2 = 1
next_number = number2
count = 1

for i in range(count,number+1):
    print(next_number, end=' ')
    number1 = number2
    number2 = next_number
    next_number = number1 + number2

print()