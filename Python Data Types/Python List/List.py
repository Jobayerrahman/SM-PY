#Integer List
nums =[12,34,54,87,96]
print(nums)


#String List
name =['Man','Tan','Rai','Ari']
print(name)
myList = ["apple","banana","cherry"]
print(myList)


#Length of A List
print(len(myList))
#The List Type
print(type(myList))


#List Constructor
yourList = list(("apple","banana","cherry"));
print(yourList)


#Check Item Exists or Not
if "apple" in yourList:
    print("yes")


#Different type of Data in a List
values = [23,'Mani',3.44]
print(values)


#List in List
mil=[nums,name]
print(mil)


#Accessing List Indexing
fruitList = ["apple","banana","cherry"];
secondItem = fruitList[1];
lastItem = fruitList[-1];                       #Negative indexing


#Slice a List
print(f'{"Positive Slice Value is : "}{nums[2:4]}')
print("Negative Slice Value is : " + str(nums[-5:-1]))


#if Item Exists
if "Mani" in name:
    print("Yes")


#Splicing List (Change List Item)
name[0:2] = ['Jhon']
print(name)


#List Method (Add List Item)
nums.append(102)
print(nums)


#List Method (Insert a List Item)
nums.insert(3,32)
print(nums)


#List Method (Extend a List with Other List)
nums.extend([21,42,78])
print(nums)



#Remove from List Item
nums.remove(12)
print(nums)
nums.pop(3)
print(nums)
nums.pop()
print(nums)

print(min(nums))

print(max(nums))

print(sum(nums))

print(sorted(name))


fruitsList = ["apple","banana","cherry","orange","mango","melon","date"];
if "apple" in fruitsList:
    print("Yes, Apple is exist in fruitsList");



