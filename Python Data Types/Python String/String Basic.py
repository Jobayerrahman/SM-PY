# strings
print('Hello')
print("World")


# quotes inside quotes
print("It's possible")
print("as long as the don't mathch")
print('the qoutes surroudig the "string"')


# assign string to a varible
a = "assigning a strinng"
print(a)


#multiline string
multiline = '''You can assign a multilie string to a variable by using three quotes'''
print(multiline)


#string are arrays
arrayString = "Hello, World!"
print(arrayString[1])


#looping through a string
for x in "banana":
    print(x)


#String length
print(len(arrayString))


#check string
txt = 'Hello world is the common word.'
print('common' in txt)

if 'common' in txt:
    print("yes")

#check not string
print('welcome' not in txt);

if 'welcome' not in txt:
    print('yes')