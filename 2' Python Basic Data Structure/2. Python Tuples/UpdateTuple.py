#Tuple
Fruitstuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(Fruitstuple)

#Convert Tuple into a List
FruitsList = list(Fruitstuple)
print(FruitsList)

#Convert List into a Tuple
FruitsList[1] = "JackFruit"
ConvertedFruitsTuple = tuple(FruitsList)
print(ConvertedFruitsTuple)

#Append method using for Tuple
FruitsList.append("avocado")
AppendedFruitsTuple = tuple(FruitsList)
print(AppendedFruitsTuple)

#Add tuple to a tuple
Vegetable = ("Tometo",)
Fruitstuple += Vegetable
print(Fruitstuple)

#Remove Item using remove method using Tuple
FruitsList.remove("orange")
RemovedFruitsTuple = tuple(FruitsList)
print(RemovedFruitsTuple)

del Fruitstuple
print(Fruitstuple)          #this will raise an error because the tuple no longer exists