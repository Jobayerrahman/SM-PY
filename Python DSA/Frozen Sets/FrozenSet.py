'''
1.Frozen sets in Python are immutable objects that only support methods and operators 
that produce a result without affecting the frozen set or sets to which they are applied. 
2.While elements of a set can be modified at any time, 
elements of the frozen set remain the same after creation.

'''

normal_set= set(["a","b","c","d"])
print(normal_set)


frozen_set= frozenset(["e","f","g"])
print(frozen_set)

