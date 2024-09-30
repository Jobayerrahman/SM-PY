#Set Operations: Given three sets A, B, and C, write a Python program to find and print the intersection of A and B, the union of B and C, and the difference between C and A.
set01 ={'Apple', 'Orange', 'Banana'}
set02 ={'JackFruits','Banana','Mango'}
set03 ={'Malon','Apple','Strawberry'}

intersectionSet = set01.intersection(set02)
unionSet = set02.union(set03)
differenceSet = set03.difference(set01)

print(intersectionSet)
print(unionSet)
print(differenceSet)