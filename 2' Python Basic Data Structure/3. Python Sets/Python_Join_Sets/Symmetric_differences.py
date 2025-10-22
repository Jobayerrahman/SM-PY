#The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set3 = {"apple","banana","google","microsoft"}

#Sets using symmetric_difference() method
print("Set items after using symmetric_difference() method: ")
symmetricDifferenceSet = set1.symmetric_difference(set2)
print(symmetricDifferenceSet)
print(" ")


#Sets using symmetric_difference ^ operator
print("Set items after using symmetric_difference ^ operator: ")
symmetricDifferenceOperatorSet = set1 ^ set2
print(symmetricDifferenceOperatorSet)
print(" ")


#symmetric_difference_update() method, keep all the duplicates, But Change the Original set.
print("Set items after using symmetric_difference_update method: ")
set3.symmetric_difference_update(set1)
print(set3)