#Sets
print("Set01 Items : ")
Set01 = {"apple","banana","cherry"}
print(Set01)
print(" ")

#Add Set Item
print("Set01 items after adding orange using add() method: ")
Set01.add("orange")
print(Set01)
print(" ")

#Add another Set
print("Set01 items after adding another set (Set02) using update() method: ")
Set02 = {"pineapple", "mango", "papaya"}
Set01.update(Set02)
print(Set01)
print(" ")

#Add any iterable
print("Set02 Items after adding any iterable (tuples, lists, dictionaries etc.) using update() method: ")
myList = ['kiwi','jackfruits']
Set02.update(myList)
print(Set02)
print(" ")

#Removing set item with remove method
print("Set01 Item Remove using remove() method : ")
Set01.remove("orange")
print(Set01)
print(" ")

#Removing set item with discard method
print("Set01 Item Remove using discard() method : ")
Set01.discard("banana")
print(Set01)
print(" ")

#Removing set item with pop method
print("Set01 Item Remove using pop() method : ")
Set01.pop()
print(Set01)
print(" ")
#Sets are unordered, so when using the pop() method, you do not know which item that gets removed

#Empty the set using clear() method
print("Set01 Item after using clear() method : ")
Set01.clear()
print(Set01)                #The clear() method empties the set
print(" ")

#Delet the set using del keyword
print("Set01 delete using del keyword : ")
del Set01                   #The del keyword will delete the set completely
print(Set01)
print(" ")