# PYTHON STRING FUNDAMENTALS

# 1. Strings in Python
# Strings are sequences of characters enclosed in either single (' ') or double (" ") quotes.
print('Hello')
print("World")

print("\n--- Quotes Inside Quotes ---")
# 2. Quotes inside quotes
print("It's possible")
print("as long as they don't match")
print('The quotes surrounding the "string"')


print("\n--- Assign String to a Variable ---")
# 3. Assign string to a variable
a = "assigning a string"
print(a)


print("\n--- Multiline String ---")
# 4. Multiline string
multiline = '''You can assign a multiline string 
to a variable by using three quotes'''
print(multiline)


print("\n--- Strings Are Arrays ---")
# 5. Strings are arrays (you can access characters by index)
arrayString = "Hello, World!"
print(arrayString[1])  # Output: e (index starts from 0)


print("\n--- Looping Through a String ---")
# 6. Looping through a string
for x in "banana":
    print(x)


print("\n--- String Length ---")
# 7. String length using len() function
print(len(arrayString))  # Output: 13


print("\n--- Check if Substring Exists ---")
# 8. Check if substring exists using 'in'
txt = 'Hello world is the common word.'
print('common' in txt)  # True

if 'common' in txt:
    print("Yes, 'common' is present in txt!")


print("\n--- Check if Substring Does Not Exist ---")
# 9. Check if substring does not exist using 'not in'
print('welcome' not in txt)  # True

if 'welcome' not in txt:
    print("Yes, 'welcome' is NOT present in txt!")

