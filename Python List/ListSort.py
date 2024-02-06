#String Sort
print('String Sort using sort() method: ')
fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort()
print(fruits)

#String reverse Sort
print('String reverse using sort() method : ')
fruits.sort(reverse = True)
print(fruits)

#String Reverse with reversr() Method
print('Reserve String using reverse() method : ')
fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.reverse()
print(fruits)

#Number Sort
print('Number Sort using sort() method : ')
number = [100, 50, 65, 82, 23]
number.sort()
print(number)

#Number Reverse
print('Number Reverse using reverse() method : ')
number.reverse()
print(number)

#Case Insensitive Sort
caseInsensitiveFruits = ["banana", "Orange", "Kiwi", "cherry"]
caseInsensitiveFruits.sort()
print(caseInsensitiveFruits)
caseInsensitiveFruits.sort(key = str.lower)
print(caseInsensitiveFruits)


#Customize Sort Function
def myfunc(n):
  return abs(n - 50)

list = [100, 50, 65, 82, 23]
list.sort(key = myfunc)
print(list)