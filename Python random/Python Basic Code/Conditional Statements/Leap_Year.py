# Leap Year Checker: Write a Python program that takes a year as input and determines if it is a leap year or not.

year = int(input("Enter the year : "))

if year%400 == 0 or year%100 != 0 and year%4 == 0:
    print(year, " Given Year is a leap Year")
else:
    print(year, " Given Year is not a leap Year")