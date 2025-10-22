#Vowel or Consonant: Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.

character = str(input("Enter the character : "))


if len(character) == 1:
    if character =='a' or character =='e' or character =='i' or character =='o' or character =='u':
        print(f"{character} is a vowel!")
    else:
        print(f"{character} is a consonant!")
else:
    print("Please enter a single character to continue\n")