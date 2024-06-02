var = 0

if var > 0:
    print("Positive")
elif var < 0:
    print("Negative")
else:
    print("Zero")



print("\nPython if elif & else")
number = int(input("Enter any number: "))

if number > 0:
    print("Your number is a Positive number!")
elif number < 0:
    print("Your number is a Negative number!")
else:
    print("Your number is zero")


a = 10
b = 6
print("\nPython Short Hand if:")
if a > b: print("a greater then b")


print("\nPython Short Hand if else:")
print("a greater then b") if a > b else print("b greater then a")
