#Looping through a list
fruits = ["apple", "banana", "cherry"]
print("\nLooping through a list: ")
for x in fruits:
    print(x)

#Looping through a string
print("\nLooping through a string: ")
for x in "banana":
    print(x)


#The break statement
#With the break statement we can stop the loop before it has looped through all the items
print("\nThe break Statement: ")
for x in fruits:
    print(x)
    if x == "banana":
        break

#Exit the loop when x is "banana", but this time the break comes before the print
print("\nThe break Statement: ")
for x in fruits:
  if x == "banana":
    break
  print(x)

#The continue statement
#With the continue statement we can stop the current iteration of the loop, and continue with the next
print("\nThe continue Statement: ")
for x in fruits:
    if x == "banana":
        continue
    print(x)

#The range() function (by default)
print("\nThe range() Function: ")
for x in range(6):
    print(x)

#The range() function (set range)
print("\nThe range() Function setting range: ")
for x in range(2,6):
    print(x)

#The range() function (set range and increment)
print("\nThe range() Function increment with 3 (by default 1): ")
for x in range(2,30,3):
    print(x)

#The else keyword 
print("\nThe else keyword: ")
for x in range(6):
    print(x)
else:
    print("finally finished!")

#The else block will Not be executed if the loop is stopped by a break statement
print("\nThe else keyword: ")
for x in range(6):
    if x ==3:break
    print(x)
else:
    print("Will not execute")

#Nested for loop
adj = ['red','green','blue']
print("\nNested loop: ")
for x in adj:
    for y in fruits:
        print(x,"-",y)

#The pass Statement
print("\nThe pass Statement 'Nothing will pass'")
for x in [0,2,3,5]:
    pass
