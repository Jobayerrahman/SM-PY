Fruitstuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(Fruitstuple)

#Loop Through a Tuple
print("Loop Through a Tuple with for loop: ")
for x in Fruitstuple:
    print(x)


#Loop Through a Tuple using range() and len() method
print("New Items with range() and len() method: ")
for i in range(len(Fruitstuple)):
    print(Fruitstuple[i])


#While Loop Through a Tuple
print("Loop Through a Tuple with while loop: ")
FruitTuple = ("apple","banana","cherry")
i = len(FruitTuple) - 1
while i > -1:
    print(FruitTuple[i])
    i = i - 1



