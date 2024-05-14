# Creating a Tuple with the use of Strings
Tuple = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple)

#Creating a Tuple with the use of List
List = [1,2,3,4,5,6]
print("\nTuple using List: ")
CovertedTuple = tuple(List)
print(CovertedTuple)


# Accessing element using indexing
print("First element of tuple")
print(CovertedTuple[0])

# Accessing element from last (negative indexing)
print("\nLast element of tuple")
print(CovertedTuple[-1])

print("\nThird last element of tuple")
print(CovertedTuple[-3])

'''
1.Python tuples are similar to lists but Tuples are immutable in nature i.e. 
2.Once created it cannot be modified. 
3.Just like a List, a Tuple can also contain elements of various types.
'''