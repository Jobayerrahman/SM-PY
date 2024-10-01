#Set Membership Test: Write a Python program that takes an element as input and checks if it exists in a given set. Print “Found” if the element is present and “Not Found” otherwise.
number = int(input('Enter the number here : '))

Set01 = {1,2,4,5,7,223,12,3,65,23,214,342}
flag = False

List = list(Set01)

for i in range(0,len(List)):
    if List[i] == number:
        flag = True
        break

if flag:
    print('Found')
else:
    print('Not Found')