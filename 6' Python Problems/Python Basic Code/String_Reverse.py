str = str(input('Enter The Original String :'))


#Reverse a string in Python using a loop
def loopReverse(str):
    rstr = ''
    for i in str:
        rstr = i + rstr
    return rstr

#Reverse a string in Python using recursion
def recursionReverse(str):
    if len(str) == 0:
        return str
    else:
        return recursionReverse(str[1:]) + str[0]

#Reverse string in Python using an extended slice
def extendedReverse(str):
    string = str[::-1]
    return string


print("The Original String is :", end='')
print(str)


print("The  Loop Reverse String is :", end='')
print(loopReverse(str))

print("The Recursion Reverse String is :", end='')
print(recursionReverse(str))

print("The Extended Reverse String is :", end='')
print(extendedReverse(str))
