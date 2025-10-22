#Set Superset Check: Given two sets A and B, write a Python program to check if set A is a superset of set B and print the result.
Set01 ={'Apple','Melon','Orange','Strawberry','Berry','Banana','Mango'}
Set02 ={'Banana','Berry','Melon','Mango'}

print('Set01 is subset of Set02 : ',Set01.issuperset(Set02))
print('Set02 is subset of Set01 : ',Set02.issuperset(Set01))