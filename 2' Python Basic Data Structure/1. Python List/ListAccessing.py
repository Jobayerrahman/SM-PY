#Accessing List
fruitList = ["apple","banana","cherry"];
secondItem = fruitList[1];
lastItem = fruitList[-1];

#List Method
#Slice a List
print(f'{"Positive Slice Value is : "}{nums[2:4]}')
print("Negative Slice Value is : " + str(nums[-5:-1]))

#if Item Exists
if "Manisha" in name:
    print("Yes")

#Splicing List (Change List Item)
name[0:2] = ['Jhon']
print(name)

fruitsList = ["apple","banana","cherry","orange","mango","melon","date"];
if "apple" in fruitsList:
    print("Yes, Apple is exist in fruitsList");