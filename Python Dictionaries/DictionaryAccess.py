#Python Dictionaries
CarDictionary ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print("Car Dictionary : ")
print(CarDictionary)
print(" ")

print("Car Dictionary Model Item Access : ")
print(CarDictionary["model"])
print(" ")

print("Car Dictionary Model Item Access Using get() Method : ")
print(CarDictionary.get("model"))
print(" ")

print("Car Dictionary Item's Keys Access Using keys() Method : ")
print(CarDictionary.keys())
print(" ")

print("Car Dictionary Item's Values Access Using values() Method : ")
print(CarDictionary.values())
print(" ")

print("Car Dictionary Items Access Using items() Method : ")
print(CarDictionary.items())
print(" ")

#if key exists
print("Car Dictionary Item's Key Exists or not : ")
if "model" in CarDictionary:
    print("Yes! Model is exist in Car Dictionary.")