'''
1.Python set is a mutable collection of data that does not allow any duplication. 
2.Sets are basically used to include membership testing and eliminating duplicate entries. 
3.The data structure used in this is Hashing, 
a popular technique to perform insertion, deletion, and traversal in O(1) on average. 
4.If Multiple values are present at the same index position, 
then the value is appended to that index position, to form a Linked List. 
5.In, CPython Sets are implemented using a dictionary with dummy variables, 
where key beings the members set with greater optimizations to the time complexity.
'''

Set = set([1,2,'Geeks',4,'For',6,'Geeks'])
print("\nSet with the use of Mixed Values")
print(Set)

#Accessing elements using for loop
print('\nElements of set: ')
for i in Set:
    print(i,end=' ')
print()

#Checking the element
print('Geeks'in Set)