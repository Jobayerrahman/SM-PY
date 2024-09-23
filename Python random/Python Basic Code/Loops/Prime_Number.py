#Prime Number Checker: Write a Python program using a while loop to check if a given number N is prime or not.

number = int(input("Enter the number : "))
count  = 2
flag   = False

if number == 0 or number == 1:
    print(number, " is not a prime number")
elif number > 1:  
    while count * count <= number:
        if (number % count) == 0:
            flag = True
            break

        else:
            flag = False

        count += 1

if flag:
    print(number, " is not a prime number")
else:
    print(number, " is a prime number")