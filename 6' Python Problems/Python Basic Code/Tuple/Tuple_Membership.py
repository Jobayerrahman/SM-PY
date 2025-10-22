#Tuple Membership Test: Write a Python program that takes an element as input and checks if it exists in a given tuple.
Tuple = (21,23,24,51,45,1,5,67,845,32,4,2,6)

randomNumber = int(input('Enter the random number : '))

List = list(Tuple)

Flag = False

for i in range(0,len(List)):
    if List[i] == randomNumber:
        Flag = True
        break


if Flag == True:
    print('Given number is a member of this tuple')
else:
    print('Given number is not a member of this tuple')