#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set3 = {"apple","banana","google","microsoft"}


#Join Two Sets using difference() method
print("Set03 items after joining two sets using difference() method: ")
differenceSet = set1.difference(set2)
print(differenceSet)
print(" ")


#Join two sets using - difference operator
print("Set03 items after joining two sets using - operator: ")
differenceOperatorSet = set1 - set2
print(differenceOperatorSet)
print(" ")


#difference_update() method, keep the items from the first set that not in the other set, But Change the Original set.
print("keeping ONLY the duplicates using intersection_update() method: ")
set3.difference_update(set1)
print(set3)
print(" ")