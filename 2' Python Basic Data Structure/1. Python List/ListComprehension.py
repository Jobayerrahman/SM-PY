List01 = [29,38,53,64,71]
List02 = []

print("List01 Items : " + str(List01))
for x in List01:
    print("List01 Item in x : " + str(x))
    if x > 40:
        List02.append(x)

print(f'{"List02 Items : "}{List02}')


print("String Comprehension ----> ")
StringList01 = ["apple", "banana", "cherry", "kiwi", "mango"]
StringList02 = []



for fruits in StringList01:
    if "a" in fruits:
        StringList02.append(fruits)

print(f'{"StringList02 Items : "}{StringList02}')

StringList03 = [x for x in StringList01 if "b" in x]
print(f'{"StringList03 Items : "}{StringList03}')