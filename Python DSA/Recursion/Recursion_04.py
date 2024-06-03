#The factorial of 6 is denoted as 6! = 1*2*3*4*5*6 = 720

def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n-1)


#Driver Code
num = int(input("Enter the number: "))

if num < 0:
    print("Invalid input! Please input a positive value")
elif num == 0:
    print("Factorial of number 0 is 1")
else:
    print(f"Factorial of number {num} is {recursive_factorial(num)}")