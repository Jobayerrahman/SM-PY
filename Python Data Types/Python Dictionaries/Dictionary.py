#Python Dictionaries
CarDictionary ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print("Car Dictionary : ")
print(CarDictionary)
print(" ")

print("Car Dictionary brand Item : ")
print(CarDictionary["brand"])
print(" ")

NotAllowDuplicateDictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 1964,
}

print("Car Dictionary Not Allow Duplicate Item in Dictionary : ")
print(NotAllowDuplicateDictionary)
print(" ")

print("Car Dictionary Length : ")
print(len(CarDictionary))
print(" ")

print("Dictionary Data Type : ")
print(type(CarDictionary))
print(" ")

print("Dictionary Constructor : ")
PersonDictionary = dict(name="Jhon", age=26, country = "Norway")
print(PersonDictionary)
print(" ")