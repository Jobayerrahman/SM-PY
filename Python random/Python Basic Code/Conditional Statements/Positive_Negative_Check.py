#Positive, Negative, or Zero: Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.

number = int(input("Enter the number : "))

if number < 0:
    print(number," Number is negative!")
elif number > 0:
    print(number," Number is positive!")
else:
    print(number," Number is zero!")