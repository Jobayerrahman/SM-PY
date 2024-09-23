#Factorial Calculator: Write a Python program using a while loop to calculate the factorial of a given number N.

number = int(input('Enter the number : '))
factorial = 1

if number < 0:
    print('Sorry, factorial does not exist for negative numbers')

elif number == 0:
    print('The factorial of 0 is 1')

else:
    for i in range(1, number+1):
        factorial = factorial * i
    print("The factorial of",number,"is",factorial)