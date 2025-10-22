#Set Symmetric Difference: Given two sets A and B, write a Python program to find the symmetric difference between the two sets (i.e., elements that are present in either set A or set B, but not in both) and print the result.

set01 ={'Apple', 'Orange', 'Banana'}
set02 ={'JackFruits','Banana','Mango'}

set03 = set01.symmetric_difference(set02)
set04 = set01 ^ set02

print(set03)
print(set04)