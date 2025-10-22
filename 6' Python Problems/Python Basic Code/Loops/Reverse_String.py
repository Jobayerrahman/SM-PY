#Reverse String: Write a Python program using a while loop to reverse a given string.

string = str(input('Enter the string to reverse: '))

strList = list(string)
lenStrList = len(strList)

revsString = ''
revsList=[]


while lenStrList > 0:
    revsList.append(strList[lenStrList-1])
    lenStrList -= 1

revsString = ''.join(revsList)
print(revsString)