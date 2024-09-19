#Largest of Three Numbers: Write a Python program that takes three numbers as input and prints the largest among them.

number01 = int(input("Enter the number 01 :"))
number02 = int(input("Enter the number 02 :"))
number03 = int(input("Enter the number 03 :"))


if number01 > number02 and number01 > number03:
    print(number01, "Number 01 is the largest number")
elif number02 > number01 and number02 > number03:
    print(number02, "Number 02 is the largest number")
else:
    print(number03, "Number 03 is the largest number")