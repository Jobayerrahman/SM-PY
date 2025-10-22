#String Palindrome: Write a Python function to check if a given string is a palindrome or not.

def checkPalindrome(string):
    return string == string[::-1]


stringValue = str(input('Enter the string : '))
checkPalindrome(stringValue) 

if checkPalindrome:
    print('Yes, Given string is a palindrome')
else:
    print('No, Given string is not a palindrome')