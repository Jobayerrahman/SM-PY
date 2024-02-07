nums =[12,34,54,87,96]
print(nums)

name =['Manisha','Tanisha','Raiyan','Ariyan']
print(name)

myList = ["apple","banana","cherry"]
yourList = list(("apple","banana","cherry"));

if "apple" in yourList:
    print("yes")
     
print(myList)
print(len(myList))
print(type(myList))
print(yourList)

#Different type of Data
values = [23,'Manisha',3.44]
print(values)

mil=[nums,name]
print(mil)

#Accessing List
print(nums[1])

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


#List Method (Add List Item)
nums.append(102)
print(nums)

nums.insert(3,32)
print(nums)

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

