#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

#Join with + Operator
print('Join with + Operator')
list3 = list1 + list2
print(list3)

#Join with append() method
for x in list2:
    list1.append(x)

print(list1)

#Join with extend() method
list1.extend(list2)
print(list1)