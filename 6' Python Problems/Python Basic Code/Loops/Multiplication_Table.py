#Table of a Number: Write a Python program using a for loop to print the multiplication table of a given number N.

number = int(input("Enter the number : "))

for i in range(1,11):
    print(i ,' x ', number, ' = ', i * number)