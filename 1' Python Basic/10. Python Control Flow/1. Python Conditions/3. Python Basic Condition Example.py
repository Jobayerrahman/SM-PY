# ---------------------- Real-life Example: Positive Negative Number ----------------------

print("\nPositive Negative Number Check")
number = int(input("Enter any number: "))

if number > 0:
    print("✅ Positive number")
elif number < 0:
    print("✅ Negative number")
else:
    print("✅ Zero")




# ---------------------- Real-Life Example: Login System ----------------------


password = "12345"

print("\nLogin System")
user_input = input("Enter password: ")

if user_input == password:
    print("✅ Login successful!")
else:
    print("❌ Wrong password")
