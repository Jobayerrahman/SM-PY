#Sum of Even Numbers: Write a Python program using a while loop to calculate the sum of all even numbers between 1 and N, where N is taken as input from the user.

number = int(input("Enter the given number : "))
count  = 0
result = 0

while count <= number:
    if count % 2 == 0:
        result = result + count
    count += 1

print(result)