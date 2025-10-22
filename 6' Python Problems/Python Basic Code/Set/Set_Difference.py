#Set Difference: Given two sets A and B, write a Python program to find the difference between set A and set B (i.e., elements present in A but not in B) and print the result.


set01 ={'Apple', 'Orange', 'Banana'}
set02 ={'JackFruits','Banana','Mango'}

set03 = set01.difference(set02)
set04 = set01 - set02

print(set03)
print(set04)