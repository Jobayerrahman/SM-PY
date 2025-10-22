#Grades Classification: Write a Python program that takes a student’s percentage as input and prints their corresponding grade according to the following criteria: 
# – 90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail

number = int(input("Enter the number : "))

if number >= 90 :
    print("A+")
elif number <= 89 and number >= 80:
    print("A-")
elif number <= 79 and number >= 70:
    print("B")
elif number >= 60 and number <= 69:
    print("C")
elif number < 60:
    print("Fail")