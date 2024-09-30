#Set Union: Given two sets A and B, write a Python program to find their union and print all the distinct elements from both sets.
set01 ={'Apple', 'Orange', 'Banana'}
set02 ={'JackFruits','Banana','Mango'}

set03 = set01.union(set02)
set04 = set01 | set02

print(set03)
print(set04)