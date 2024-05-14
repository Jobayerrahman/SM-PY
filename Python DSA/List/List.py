List = [1,2,3,"GG",2.4]
print(List)

#Creating a List with the use of multiple values
multipleValueList = ['Geeks', 'for', "Geeks"]
print("\nList containing multiple values: ")
print(multipleValueList)

# Creating a Multi-Dimensional List
multiDimenstionalList = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")
print(multiDimenstionalList)

# Accessing a element from the list using index number
print("Accessing element from the list")
print(List[0])
print(List[2])

# Accessing a element using negative indexing
print("Accessing element using negative indexing")
# print the last element of list
print(List[-1])
# print the third last element of list
print(List[-3])

'''
1.Python Lists are ordered collections of data just like arrays in other programming languages. 

2.It allows different types of elements in the list. 

3.The implementation of Python List is similar to Vectors in C++ or ArrayList in JAVA. 

4.The costly operation is inserting or deleting the element from the beginning of the List, 
as all the elements are needed to be shifted. 

5.Insertion and deletion at the end of the list can also become costly, 
in the case where the preallocated memory becomes full.

6.List elements can be accessed by the assigned index. 

7.In python starting index of the list, 
a sequence is 0 and the ending index is (if N elements are there) N-1.
'''