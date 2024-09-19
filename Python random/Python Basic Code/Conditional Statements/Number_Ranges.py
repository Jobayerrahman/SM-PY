#Number Ranges: Write a Python program that takes an integer as input and prints whether the number falls within the 
# ranges: 0-50, 51-100, 101-150, or above 150.

number = int(input("Enter the number : "))

if number >=0 and number <=50:
    print("Given number is the range of 0-50")
elif number >=51 and number <=100:
    print("Given number is the range of 51-100")
elif number >=101 and number <=150:
    print("Given number is the range of 101-150")
else:
    print("Given number is above 150")