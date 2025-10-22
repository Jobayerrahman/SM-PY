#Sum of N Numbers: Write a Python program using a for loop to calculate the sum of the first N natural numbers, where N is taken as input from the user.

number  = int(input("Enter the number : "))

if number < 0 :
    print('Enter a positive number')
else:
    sum = 0
    # while(number > 0):
    #     sum = sum + number
    #     number = number - 1
    for i in range(number+1):
        sum = sum + i
        print(sum)

    print('The sum is : ', sum)
