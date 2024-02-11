#Sets
Set01 = {"apple","banana","cherry"}
print(Set01)

#Duplicates Not Allowed
Set02 = {"apple","banana","cherry","apple"}
print(Set02)

#True and 1 is considered the same value
Set03 = {"apple", "banana", "cherry", True, 1, 2}
print(Set03)

#False and 0 is considered the same value
Set04 = {"apple", "banana", "cherry", False, 1, 0}
print(Set04)

#Length method
print(len(Set01))

#Different data types in one set
Set05 = {"abc", 34, True, 40, "male"}
print(Set05)

#Set type
print(type(Set01))
print(type(Set05))

#The set() Constructor
ConstructorSet = set(("a", "b", "c"))
print(ConstructorSet)
