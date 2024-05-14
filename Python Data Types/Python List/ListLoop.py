number = [12,43,52,13,5,67]
print(number)

print("For Loop Value of List : ")
for x in number:
    print(x)

print("For Loop Value of List with Range and Length : ListName[item]")
for x in range(len(number)):
    print(number[x]);

print("While Loop Value of List  : ")
i = len(number) - 1
while i > -1:
    print(number[i])
    i = i - 1


print("Looping Using List Comprehension : ")
[print(x) for x in number]