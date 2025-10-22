'''
✅ 1. if Statement
        - Used when you want to check only one condition.
'''

temperature = 35

if temperature > 30:
    print("It's a hot day!")



'''
✅ 2. if else Statement
        - Used when you need two possible outcomes.
'''

age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You are not eligible to vote.")


'''
✅ 3. if elif else Statement
        - Used when you need to check multiple conditions.
'''

marks = 75

if marks >= 80:
    print("Grade: A+")
elif marks >= 60:
    print("Grade: A")
elif marks >= 50:
    print("Grade: B")
else:
    print("Grade: Fail")


# ---------------------- Real-life Example: Bank Balance Check ----------------------


balance = 500

if balance > 0:
    print("Your account is active.")
else:
    print("Your account is empty.")

