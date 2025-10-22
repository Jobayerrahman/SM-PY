#Tuple
Fruitstuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(Fruitstuple)

#Accessign Tuple Item
print(Fruitstuple[2])

#Negative Indexing
print(Fruitstuple[-2])

#Range of Positive Indexes
print(Fruitstuple[1:5])

#Range of Positive Indexes Start Position
print(Fruitstuple[2:])

#Range of Positive Indexes End Position
print(Fruitstuple[:5])

#Range of Negative Indexes
print(Fruitstuple[-5:-1])

#Range of Negative Indexes Start Position
print(Fruitstuple[-2:])

#Range of Negative Indexes End Position
print(Fruitstuple[:-2])

#Check if Item Exists
if "apple" in Fruitstuple:
    print('yes! apple is exists')