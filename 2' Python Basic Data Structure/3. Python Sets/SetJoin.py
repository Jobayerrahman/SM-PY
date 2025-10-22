#set
Set01 = {"a","b","c","d"}
Set02 = {1,2,3,12}
Set03 = {"a","b","c","d","aa","bb","cc","dd"}
Set04 = {"string",False,"number",12,True,3}
Set05 = {"a","d","aa","cc",}

#Join Two Sets using union() method
print("Set01 items after joining two sets using union() method: ")
unionSet = Set01.union(Set02)
print(unionSet)
print(" ")

print("Set01 items after joining multiple sets using union() method: ")
unionMultipleSet = Set01.union(Set02,Set03,Set04)
print(unionMultipleSet)
print(" ")

print("Set01 items after joining two sets using union() method: ")
unionOperatorSet = Set01 | Set02
print(unionOperatorSet)
print(" ")

print("Set items after joining multiple sets using | operator: ")
unionOperatorMultipleSet = Set01 | Set02 | Set03 | Set04
print(unionOperatorMultipleSet);
print(" ")


#Join Two Sets using update() method
print("Set01 items after joining two sets using update() method: ")
updateSet = Set01.union(Set02)
print(updateSet)
print(" ")

#Keeping ONLY the Duplicates
print("keeping ONLY the duplicates using intersection() method: ")
intersectionSet = Set01.intersection(Set03)
print(intersectionSet)
print(" ")


print("keeping ONLY the duplicates using & operator: ")
intersectionOperatorSet = Set01 & Set03
print(intersectionOperatorSet)
print(" ")


#intersection_update() method, keep ONLY the Duplicates, But Change the Original set.
print("keeping ONLY the duplicates using intersection_update() method: ")
Set05.intersection_update(Set03)
print(Set05)
print(" ")
