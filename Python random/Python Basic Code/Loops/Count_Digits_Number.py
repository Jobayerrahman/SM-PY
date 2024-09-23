#Count Digits in a Number: Write a Python program using a while loop to count the number of digits in a given integer N.

number = int(input("Enter the number : "))
count = 0

while number != 0:
    number //=10
    count += 1

print("Number of digits: " + str(count)) 